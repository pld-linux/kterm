Summary:	A Kanji (Japanese character set) terminal emulator for X
Summary(pl):	Emulator terminala Kanji (z japoñskimi znakami) dla X
Name:		kterm
Version:	6.2.0
Release:	8
License:	distributable
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.sunet.se/pub/X11/R6contrib/applications/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-6.2.0-kbd.patch
Patch1:		%{name}-6.2.0-glibc.patch
Patch2:		%{name}-6.2.0-utmp98.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	utempter

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%description -l pl
Pakiet kterm zawiera emulator terminala z japoñskim zestawem znaków
Kanji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/kterm.desktop

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kterm
%{_libdir}/X11/app-defaults/KTerm
%{_mandir}/man1/kterm.1x*
%{_sysconfdir}/X11/wmconfig/kterm

%clean
rm -rf $RPM_BUILD_ROOT
