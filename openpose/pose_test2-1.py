# 직선 0-1 과 1-8 사이의 각도 (angle1), 직선 0-1과 1-9 사이의 각도(angle2)를 계산하는 버전
import cv2
import math

# 각도 계산 함수
def calculate_angle(x1, y1, x2, y2, x3, y3):
    # 두 점 (x1, y1)와 (x2, y2) 사이의 벡터
    vector1 = (x2 - x1, y2 - y1)
    # 두 점 (x2, y2)와 (x3, y3) 사이의 벡터
    vector2 = (x3 - x2, y3 - y2)

    # 벡터의 내적을 계산
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    # 벡터의 크기를 계산
    magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
    magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

    # 두 벡터의 각도를 라디안에서 계산
    angle = math.acos(dot_product / (magnitude1 * magnitude2))

    # 라디안 값을 도로 변환
    angle_degrees = math.degrees(angle)

    return angle_degrees

def output_keypoints(frame, proto_file, weights_file, threshold, model_name, BODY_PARTS):
    global points

    # 네트워크 불러오기
    net = cv2.dnn.readNetFromCaffe(proto_file, weights_file)

    # 입력 이미지의 사이즈 정의
    image_height = 368
    image_width = 368

    # 네트워크에 넣기 위한 전처리
    input_blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (image_width, image_height), (0, 0, 0), swapRB=False, crop=False)

    # 전처리된 blob 네트워크에 입력
    net.setInput(input_blob)

    # 결과 받아오기
    out = net.forward()
    # The output is a 4D matrix
    out_height = out.shape[2]
    # The fourth dimension is the width of the output map.
    out_width = out.shape[3]

    # 원본 이미지의 높이, 너비를 받아오기
    frame_height, frame_width = frame.shape[:2]

    # 포인트 리스트 초기화
    points = []

    print(f"\n============================== {model_name} Model ==============================")
    for i in range(len(BODY_PARTS)):

        # 신체 부위의 confidence map
        prob_map = out[0, i, :, :]

        # 최소값, 최대값, 최소값 위치, 최대값 위치
        min_val, prob, min_loc, point = cv2.minMaxLoc(prob_map)

        # 원본 이미지에 맞게 포인트 위치 조정
        x = (frame_width * point[0]) / out_width
        x = int(x)
        y = (frame_height * point[1]) / out_height
        y = int(y)

        if prob > threshold:  # [pointed]
            cv2.circle(frame, (x, y), 5, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, lineType=cv2.LINE_AA)

            points.append((x, y))
            print(f"[pointed] {BODY_PARTS[i]} ({i}) => prob: {prob:.5f} / x: {x} / y: {y}")

        else:  # [not pointed]
            cv2.circle(frame, (x, y), 5, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, lineType=cv2.LINE_AA)

            points.append(None)
            print(f"[not pointed] {BODY_PARTS[i]} ({i}) => prob: {prob:.5f} / x: {x} / y: {y}")

    cv2.imshow("Output_Keypoints", frame)
    cv2.waitKey(0)

    # 각도 계산
    x1 = points[0][0]  # nose(0)
    y1 = points[0][1]
    x2 = points[1][0]  # neck(1)
    y2 = points[1][1]
    x8 = points[8][0]  # rhip(8)
    y8 = points[8][1]
    x9 = points[9][0]  # lhip(9)
    y9 = points[9][1]

    angle1 = calculate_angle(x1, y1, x2, y2, x8, y8)
    print(f"angle1 : {angle1}")
    angle2 = calculate_angle(x1, y1, x2, y2, x9, y9)
    print(f"angle2 : {angle2}")

    return frame

def output_keypoints_with_lines(frame, POSE_PAIRS):
    print()
    for pair in POSE_PAIRS:
        part_a = pair[0]  # 0 (Head)
        part_b = pair[1]  # 1 (Neck)
        if points[part_a] and points[part_b]:
            print(f"[linked] {part_a} {points[part_a]} <=> {part_b} {points[part_b]}")
            cv2.line(frame, points[part_a], points[part_b], (0, 255, 0), 3)
        else:
            print(f"[not linked] {part_a} {points[part_a]} <=> {part_b} {points[part_b]}")

    cv2.imshow("output_keypoints_with_lines", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


BODY_PARTS_COCO = {0: "Nose", 1: "Neck", 2: "RShoulder", 3: "RElbow", 4: "RWrist",
                   5: "LShoulder", 6: "LElbow", 7: "LWrist", 8: "RHip", 9: "RKnee",
                   10: "RAnkle", 11: "LHip", 12: "LKnee", 13: "LAnkle", 14: "REye",
                   15: "LEye", 16: "REar", 17: "LEar", 18: "Background"}

POSE_PAIRS_COCO = [[0, 1], [0, 14], [0, 15], [1, 2], [1, 5], [1, 8], [1, 11], [2, 3], [3, 4],
                   [5, 6], [6, 7], [8, 9], [9, 10], [12, 13], [11, 12], [14, 16], [15, 17]]


# 신경 네트워크의 구조를 지정하는 prototxt 파일 (다양한 계층이 배열되는 방법 등)
protoFile_coco = "openpose-master\\openpose-master\\models\\pose\\coco\\pose_deploy_linevec.prototxt"

# 훈련된 모델의 weight 를 저장하는 caffemodel 파일
weightsFile_coco = "openpose-master\\openpose-master\\models\\pose\\coco\\pose_iter_440000.caffemodel"

# 이미지 경로
image = "public\\sitting.png"

# 키포인트를 저장할 빈 리스트
points = []

# 이미지 읽어오기
frame_mpii = cv2.imread(image)
frame_coco = frame_mpii.copy()
frame_body_25 = frame_mpii.copy()


# COCO Model
frame_COCO = output_keypoints(frame=frame_coco, proto_file=protoFile_coco, weights_file=weightsFile_coco,
                             threshold=0.2, model_name="COCO", BODY_PARTS=BODY_PARTS_COCO)
output_keypoints_with_lines(frame=frame_COCO, POSE_PAIRS=POSE_PAIRS_COCO)
