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

//String Handling
#include <sstream>
#include <string>


//Message Handling
LRESULT CALLBACK WindowProc(
    __in HWND hWindow,
    __in UINT uMsg,
    __in WPARAM wParam,
    __in LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_CLOSE:
        PostQuitMessage(69);
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    case WM_KEYDOWN:
        if (wParam == 'W')
        {
            SetWindowText(hWindow, "W");
        }
        else if (wParam == 'A')
        {
            SetWindowText(hWindow, "A");
        }
        else if (wParam == 'S')
        {
            SetWindowText(hWindow, "S");
        }
        else if (wParam == 'D')
        {
            SetWindowText(hWindow, "D");
        }
        break;
    case WM_KEYUP:
        SetWindowText(hWindow, "The One");
        break;
    default:
        return DefWindowProc(hWindow, uMsg, wParam, lParam);
    }

    return 0;
}


// Main Function Window instance
int CALLBACK WinMain(
  HINSTANCE hInstance,
  HINSTANCE prevInstance,
  LPSTR lpCmdLine,
  int nCmdShow)
  {

    LPCSTR pClassName = "newwindow";
    WNDCLASSEX wc = {0};
    wc.cbSize = sizeof( wc );
    wc.style = CS_OWNDC;
    wc.lpfnWndProc = WindowProc;
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
    BOOL gResult;
    while ((gResult = GetMessage( &msg,nullptr,0,0)) > 0)
    {
      TranslateMessage( &msg );
      DispatchMessage( &msg );
    }
    if (gResult == -1) //Error handling
    {
      return -1;
    }
    else
    {
      return msg.wParam;
    }
    return 0;
  }
