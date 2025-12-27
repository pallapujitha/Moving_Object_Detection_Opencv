import cv2  # Import the OpenCV library

class MotionDetector:
    def __init__(self, output_path):
        self.output_path = output_path  # Initialize the output path for the video file

    def detect_motion(self):
        cap = cv2.VideoCapture(0)  # Capture video from the webcam
        ret, frame1 = cap.read()  # Read the first frame from the webcam
        ret, frame2 = cap.read()  # Read the second frame from the webcam

        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec for the output video
        out = cv2.VideoWriter(self.output_path, fourcc, 20.0, (640, 480))  # Create a VideoWriter object to save the output video

        while cap.isOpened():  # Loop until the webcam is open
            diff = cv2.absdiff(frame1, frame2)  # Compute the absolute difference between the current and previous frames
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the difference to grayscale
            blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to reduce noise and improve contour detection
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # Apply a binary threshold to create a binary image
            dilated = cv2.dilate(thresh, None, iterations=3)  # Dilate the thresholded image to fill in holes

            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the dilated image

            for contour in contours:  # Iterate over each contour
                if cv2.contourArea(contour) < 700:  # Ignore small contours to reduce noise
                    continue
                x, y, w, h = cv2.boundingRect(contour)  # Get the bounding box for the contour
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Draw a rectangle around the contour

            image = cv2.resize(frame1, (640, 480))  # Resize the frame to match the output video size
            out.write(image)  # Write the frame to the output video
            cv2.imshow("feed", frame1)  # Display the frame in a window
            frame1 = frame2  # Update frame1 to be the previous frame
            ret, frame2 = cap.read()  # Read a new frame from the webcam

            if cv2.waitKey(40) == 27:  # Break the loop if the 'Esc' key is pressed
                break

        cap.release()  # Release the webcam
        out.release()  # Release the VideoWriter object
        cv2.destroyAllWindows()  # Close all OpenCV windows
