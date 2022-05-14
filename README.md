# Histogram_Eqalization_example

The program code was written using Python and Opencv, and it is a program source that directly implements the round method of histogram Eqalization.

해당 프로그램 코드는 Python, Opencv를 이용하여 히스토그램 평활화 알고리즘을 직접 구현하여 실행한 결과와 Opencv 의 EqalizationHist() 함수를 이용해 구현한 방식을 비교하는 프로그램 입니다.  

After converting to YCrCb color, both methods apply the histogram smoothing algorithm to the Y dimension and measure the restore rate of the original image and the restored image using PSNR (signal-to-noise ratio) after the restore.

두 방식 모두 YCrCb 색상으로 변환 후 Y 차원에 대해 히스토그램 평활화 알고리즘을 적용하고 복원 후 PSNR (신호대잡음비) 를 이용하여 원본 영상과 복원된 이미지의 복원율을 측정 합니다.

테스트에 사용된 이미지 : tesla model 3

# Program excute image

![image](https://user-images.githubusercontent.com/83262616/167287336-f9587742-0f22-45c8-9374-b4379b49a67d.png)
