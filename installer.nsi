!include "MUI2.nsh"

Name "Locator Viewer"
OutFile "LocatorViewerInstaller.exe"
InstallDir "$PROGRAMFILES64\LocatorViewer"
RequestExecutionLevel admin
SetCompressor /SOLID lzma

!ifndef APP_VERSION
    !define APP_VERSION "0.0.0.0"
!endif

VIProductVersion "${APP_VERSION}"
VIAddVersionKey "FileVersion" "${APP_VERSION}"
VIAddVersionKey "ProductVersion" "${APP_VERSION}"

VIAddVersionKey "ProductName" "Locator Viewer"
VIAddVersionKey "CompanyName" "Codeyro Production"
VIAddVersionKey "FileDescription" "Установщик Locator Viewer"
VIAddVersionKey "LegalCopyright" "© 2026 Codeyro Production"

!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_FINISHPAGE_RUN "$INSTDIR\Locator Viewer.exe"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_LANGUAGE "Russian"

Section "Install"
  SetOutPath "$INSTDIR"
  File /r "dist\Locator Viewer\*.*"
  
  CreateDirectory "$SMPROGRAMS\LocatorViewer"
  CreateShortcut "$SMPROGRAMS\LocatorViewer\Locator Viewer.lnk" "$INSTDIR\Locator Viewer.exe"
  CreateShortcut "$SMPROGRAMS\LocatorViewer\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
  CreateShortcut "$DESKTOP\Locator Viewer.lnk" "$INSTDIR\Locator Viewer.exe"
  
  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
  ExecWait 'taskkill /f /im "Locator Viewer.exe" /t' 
    
  Delete "$DESKTOP\Locator Viewer.lnk"
  Delete "$SMPROGRAMS\LocatorViewer\Locator Viewer.lnk"
  Delete "$SMPROGRAMS\LocatorViewer\Uninstall.lnk"
  RMDir "$SMPROGRAMS\LocatorViewer"

  RMDir /r "$INSTDIR"

  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\LocatorViewer"
SectionEnd
