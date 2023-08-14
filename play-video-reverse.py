import cv2

# Open the video file
video_path = r'C:\Users\NITHISH\Desktop\Opencv\image\sample.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a VideoWriter object to save the reversed video
output_path = 'reversed_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Read and write frames in reverse order
for frame_index in range(total_frames - 1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    
    # Display the reversed frame
    cv2.imshow('Reversed Video', frame)
    
    # Break loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
