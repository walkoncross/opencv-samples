using namespace cv;
Mat src = imread("../data/iloveyouticket.jpg");
Mat dst = imread("../data/wood-texture.jpg");
     
// Create an all white mask
Mat src_mask = 255 * Mat::ones(src.rows, src.cols, src.depth());
     
// The location of the center of the src in the dst
Point center(dst.cols/2,dst.rows/2);
     
// Seamlessly clone src into dst and put the results in output
Mat normal_clone;
Mat mixed_clone;
     
seamlessClone(src, dst, src_mask, center, normal_clone, NORMAL_CLONE);
seamlessClone(src, dst, src_mask, center, mixed_clone, MIXED_CLONE);
     
// Save results
imwrite("../data/opencv-normal-clone-example.jpg", normal_clone);
imwrite("../data/opencv-mixed-clone-example.jpg", mixed_clone);