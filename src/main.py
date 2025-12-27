from motion_detector import MotionDetector  # Import the MotionDetector class from the motion_detector module

if __name__ == "__main__":  # Check if this script is being run as the main program
    output_path = "../output/output_video.avi"  # Define the path where the output video will be saved
    detector = MotionDetector(output_path)  # Create an instance of the MotionDetector class with the specified output path
    detector.detect_motion()  # Call the detect_motion method to start detecting motion and saving the output video
