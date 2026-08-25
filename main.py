import argparse
import cv2
def main():
    parser = argparse.ArgumentParser(
        description="convert a color image to grayscale."
        )
    parser.add_argument("--input" , required=True)
    parser.add_argument("--output" , required=True)
    args = parser.parse_args()

    image = cv2.imread(args.input)
    gray = cv2.cvtColor(image, cv2.color_bgr2gray)
    cv2.imwrite(args.output , gray)
    print("تصویر خاکستری ذخیره شد")