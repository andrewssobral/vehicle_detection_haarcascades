@echo off

:: For drag & drop video
:: build\vehicle_detection_x86.exe cars.xml %1
:: build\vehicle_detection_x64.exe cars.xml %1

:: For Win32
build\vehicle_detection_x86.exe cars.xml dataset/video1.avi
build\vehicle_detection_x86.exe cars.xml dataset/video2.avi

:: For Win64
:: build\vehicle_detection_x64.exe cars.xml dataset/video1.avi
:: build\vehicle_detection_x64.exe cars.xml dataset/video2.avi
