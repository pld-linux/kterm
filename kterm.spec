Summary: A Kanji (Japanese character set) terminal emulator for X.
Name: kterm
Version: 6.2.0
Release: 8
Source: ftp://ftp.sunet.se/pub/X11/R6contrib/applications/kterm-6.2.0.tar.gz
Source1: kterm.wmconfig
Patch0: kterm-6.2.0-kbd.patch
Patch1: kterm-6.2.0-glibc.patch
Patch2: kterm-6.2.0-utmp98.patch
Copyright: distributable
Group: User Interface/X
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires: /usr/sbin/utempter

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%prep
%setup
%patch0 -p1 -b .kbd
%patch1 -p1 -b .glibc
%patch2 -p1 -b .utempter

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 -o root -g root $RPM_SOURCE_DIR/kterm.wmconfig \
	$RPM_BUILD_ROOT/etc/X11/wmconfig/kterm
chmod 755 $RPM_BUILD_ROOT/usr/X11R6/bin/kterm

%files
/usr/X11R6/bin/kterm
/usr/X11R6/lib/X11/app-defaults/KTerm
/usr/X11R6/man/man1/kterm.1x
/etc/X11/wmconfig/kterm

%clean
rm -rf $RPM_BUILD_ROOT
