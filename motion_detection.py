{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# download amd import library cv2.\n",
    "# pip install opencv-python.\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating video capture object to record video.\n",
    "video = cv2.VideoCapture(0)\n",
    "first_frame = None\n",
    "#using while loop to record frame-by-frame.\n",
    "while True:\n",
    "    check, frame = video.read()\n",
    "    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    grey = cv2.GaussianBlur(grey,(21,21),0)\n",
    "    if first_frame is None:\n",
    "        first_frame = grey\n",
    "        continue\n",
    "    #calculating the difference between frames to detect motion.\n",
    "    diff_frame = cv2.absdiff(first_frame, grey)\n",
    "    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]\n",
    "    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 0)\n",
    "    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n",
    "    for contour in cnts:\n",
    "        if cv2.contourArea(contour) < 500:\n",
    "            continue\n",
    "        (x,y,w,h) = cv2.boundingRect(contour)\n",
    "        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)\n",
    "    cv2.imshow(\"grey frame\", grey)\n",
    "    cv2.imshow(\"difference frame\", diff_frame)\n",
    "    cv2.imshow(\"Threshold frame\", thresh_frame)\n",
    "    cv2.imshow(\"Color frame\", frame)\n",
    "    #quit the program by pressing \"x\" button.\n",
    "    key = cv2.waitKey(1)\n",
    "    if key == ord(\"x\"):\n",
    "        break\n",
    "video.release()\n",
    "cv2.destroyAllWindows()\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
