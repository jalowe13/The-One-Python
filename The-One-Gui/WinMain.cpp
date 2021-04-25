#include <iostream>
// Windows Header Files:
#include <windows.h>

// C RunTime Header Files:
#include <stdlib.h>
#include <malloc.h>
#include <memory.h>
#include <wchar.h>
#include <math.h>

#include <d2d1.h>
#include <d2d1helper.h>
#include <dwrite.h>
#include <wincodec.h>

// Main Function Window instance
int CALLBACK WinMain(
  HINSTANCE hInstance,
  HINSTANCE prevInstance,
  LPSTR lpCmdLine,
  int nCmdShow)
  {

    LPCSTR pClassName = "Window Class";
    WNDCLASSEX wc = {0};
    wc.cbSize = sizeof( wc );
    wc.style = CS_OWNDC;
    wc.lpfnWndProc = DefWindowProc;
    wc.cbClsExtra = 0;
    wc.cbWndExtra = 0;
    wc.hInstance = hInstance;
    wc.hIcon = nullptr;
    wc.hCursor = nullptr;
    wc.hbrBackground = nullptr;
    wc.lpszMenuName = nullptr;
    wc.lpszClassName = pClassName;
    wc.hIconSm = nullptr;
    RegisterClassEx(&wc);
    HWND hWnd = CreateWindowEx(
      0,pClassName,
      "The One",
      WS_CAPTION | WS_MINIMIZEBOX | WS_SYSMENU,
      200,200,640,480,
      nullptr,nullptr,hInstance,nullptr
    );
    ShowWindow(hWnd,SW_SHOW);
    MSG msg; //New message instance
    while (GetMessage( &msg,nullptr,0,0) > 0)
    {
      TranslateMessage( &msg );
      DispatchMessage( &msg );
    }
    return 0;
  }
