Summary:	A Kanji (Japanese character set) terminal emulator for X.
Name:		kterm
Version:	6.2.0
Release:	8
Source0:	ftp://ftp.sunet.se/pub/X11/R6contrib/applications/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-6.2.0-kbd.patch
Patch1:		%{name}-6.2.0-glibc.patch
Patch2:		%{name}-6.2.0-utmp98.patch
Copyright:	distributable
Group:		X11/Applications
Group(pl):	X11/Aplikacje
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	utempter

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%prep
%setup -q
%patch0 -p1 -b .kbd
%patch1 -p1 -b .glibc
%patch2 -p1 -b .utempter

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig
install -o root $RPM_SOURCE_DIR/kterm.wmconfig \
$RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/kterm
chmod 755 $RPM_BUILD_ROOT%{_bindir}/kterm

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kterm
%{_libdir}/X11/app-defaults/KTerm
%{_mandir}/man1/kterm.1x
%{_sysconfdir}/X11/wmconfig/kterm

%clean
rm -rf $RPM_BUILD_ROOT
