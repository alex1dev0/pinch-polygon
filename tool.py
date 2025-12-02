import cv2
import mediapipe as mp
import numpy as np
import math

class AICircleTool:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        self.num_sides = 3
        self.center = (640, 360)
        self.radius = 150
        self.max_sides = 20
        self.min_sides = 3
        
        self.prev_distance = 0
        self.distance_threshold = 0.02
        self.gesture_cooldown = 0
        self.cooldown_frames = 15
        
    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
    def draw_polygon(self, image, num_sides, center, radius):
        if num_sides < 3:
            return
            
        points = []
        for i in range(num_sides):
            angle = 2 * math.pi * i / num_sides - math.pi / 2 
            x = int(center[0] + radius * math.cos(angle))
            y = int(center[1] + radius * math.sin(angle))
            points.append((x, y))

        points_array = np.array(points, np.int32)
        cv2.fillPoly(image, [points_array], (100, 200, 255))  
        cv2.polylines(image, [points_array], True, (0, 255, 255), 3)  
        
        for point in points:
            cv2.circle(image, point, 8, (0, 0, 255), -1) 
    
    def draw_ui(self, image):
        cv2.rectangle(image, (10, 10), (300, 100), (0, 0, 0), -1)
        cv2.rectangle(image, (10, 10), (300, 100), (255, 255, 255), 2)
        
        cv2.putText(image, f"Lati: {self.num_sides}", (20, 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        polygon_names = {
            3: "Triangle", 4: "Square", 5: "Pentagon", 6: "Hexagon",
            7: "Heptagon", 8: "Octagon", 9: "Enneagon", 10: "Decagon"
        }
        name = polygon_names.get(self.num_sides, f"Poligono {self.num_sides} lati")
        cv2.putText(image, name, (20, 70), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.rectangle(image, (10, 620), (600, 710), (0, 0, 0), -1)
        cv2.rectangle(image, (10, 620), (600, 710), (255, 255, 255), 2)
        cv2.putText(image, "Instructions:", (20, 645), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(image, "- Pinch thumb and index finger to add sides", (20, 665), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(image, "- Unpinch thumb and index finger to remove sides", (20, 685), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(image, "- Press 'q' to exit", (20, 705), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    def process_gesture(self, landmarks):
        if self.gesture_cooldown > 0:
            self.gesture_cooldown -= 1
            return
        
        thumb_tip = landmarks[4] 
        index_tip = landmarks[8]
        
        current_distance = self.calculate_distance(thumb_tip, index_tip)
        
        if self.prev_distance > 0:
            distance_change = current_distance - self.prev_distance
            
            if distance_change > self.distance_threshold:
                if self.num_sides < self.max_sides:
                    self.num_sides += 1
                    self.gesture_cooldown = self.cooldown_frames
                    print(f"Gesto rilevato: Allargamento - Lati: {self.num_sides}")
            
            elif distance_change < -self.distance_threshold:
                if self.num_sides > self.min_sides:
                    self.num_sides -= 1
                    self.gesture_cooldown = self.cooldown_frames
                    print(f"Gesto rilevato: Restringimento - Lati: {self.num_sides}")
        
        self.prev_distance = current_distance
    
    def run(self):
        print("PINCH POLYGON")
        print("Use the thumb and index finger to adjust the number of polygon sides.")
        print("Press 'q' to exit.")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error reading webcam frame")
                break
            
            frame = cv2.flip(frame, 1)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.hands.process(rgb_frame)
            
            self.draw_polygon(frame, self.num_sides, self.center, self.radius)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    
                    self.process_gesture(hand_landmarks.landmark)
                    
                    h, w, _ = frame.shape
                    thumb_tip = hand_landmarks.landmark[4]
                    index_tip = hand_landmarks.landmark[8]
                    
                    thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                    index_pos = (int(index_tip.x * w), int(index_tip.y * h))
                    
                    cv2.circle(frame, thumb_pos, 10, (255, 0, 0), -1)
                    cv2.circle(frame, index_pos, 10, (0, 255, 0), -1)
                    cv2.line(frame, thumb_pos, index_pos, (255, 255, 255), 2)
            
            self.draw_ui(frame)
            
            cv2.imshow('PINCH POLYGON', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    try:
        app = AICircleTool()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        print("Ensure you have installed the dependencies: pip install -r requirements.txt")
        print("And that the webcam is connected and working.")

if __name__ == "__main__":
    main()