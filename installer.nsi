!include "MUI2.nsh"

Name "Locator Viewer"
OutFile "LocatorViewerSetup.exe"
InstallDir "$PROGRAMFILES\LocatorViewer"

!insertmacro MUI_PAGE_WELCOME
!define MUI_ABORTWARNING
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_LANGUAGE "English"

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
  RMDir /r "$INSTDIR"
  RMDir /r "$SMPROGRAMS\LocatorViewer"
  Delete "$DESKTOP\Locator Viewer.lnk"
SectionEnd
