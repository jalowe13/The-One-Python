#include "Graphics.h"
#pragma comment(lib, "d2d1")
//Specify library ^^
Graphics::Graphics()
{
  factory = NULL;
  renderTarget = NULL;
}

Graphics::~Graphics()
{
  if(factory) factory->Release();
  if(renderTarget) renderTarget->Release();
}

bool Graphics::Init(HWND windowHandle)
{
  HRESULT res = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED,
                                  &factory); //Creates a new Factory
  if(res != S_OK) return false; //IF the factory creation is not okay

  RECT rect; //Create new Rectangle
  GetClientRect(windowHandle, &rect);
  factory->CreateHwndRenderTarget(
    D2D1::RenderTargetProperties(),
    D2D1::HwndRenderTargetProperties(
      windowHandle, D2D1::SizeU(rect.right, rect.bottom)),
      &renderTarget);
  if(res != S_OK) return false;
   return true;
}

void Graphics::ClearScreen(float r, float g, float b)
{
    renderTarget->Clear(D2D1::ColorF(r, g, b)); //Clear screen
}

void Graphics::DrawCircle(float x, float y, float rad, float r, float g, float b, float a)
{
    ID2D1SolidColorBrush* brush; //Create new color brush
    renderTarget->CreateSolidColorBrush(D2D1::ColorF(r, g, b, a), &brush);
    renderTarget->DrawEllipse(D2D1::Ellipse(D2D1::Point2F(x, y), rad, rad), brush, 2.0f);
    brush->Release();
}

void Graphics::DrawFPS(float x, float y, float rad, float r, float g, float b, float a)
{
    wchar_t* txt = L"Hello World";
  IDWriteTextLayout* pTextLayout_;
  ID2D1SolidColorBrush* brush; //Create new color brush
  renderTarget->CreateSolidColorBrush(D2D1::ColorF(r, g, b, a), &brush);
}
