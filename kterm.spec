Summary:	A Kanji (Japanese character set) terminal emulator for X
Summary(de):	Kterm (Kanji-Terminal-Emulator)
Summary(es):	Kterm (Emulador de Terminal Kanji)
Summary(fr):	Kterm (Émulateur de terminal Kanji)
Summary(ja):	ÆüËÜ¸ì¤ÎÉ½¼¨¤¬²ÄÇ½¤Ê X ¾å¤Î¥¿¡¼¥ß¥Ê¥ë¥½¥Õ¥È¤Ç¤¹
Summary(pl):	Emulator terminala Kanji (z japoñskimi znakami) dla X
Summary(pt_BR):	Kterm (Emulador de Terminal Kanji)
Summary(tr):	Kanji uçbirim öykünümcüsü
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
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%description -l de
kterm ist der Kanji-Terminal-Emulator. Statt des normalen englischen
Zeichensatzes arbeitet er mit dem japanischen Kanji-System.

%description -l es
kterm es el Emulador de Terminal Kanji. Usa el conjunto de caracteres
Kanji en lugar del conjunto normal de inglés para aquellos que
prefieran Kanji.

%description -l fr
kterm est l'émulateur de terminal Kanji. Il utilise les caractères
Kanji à la place des caractères français normaux.

%description -l ja
ÆüËÜ¸ì¤ÎÉ½¼¨¤¬²ÄÇ½¤Ê X ¾å¤Î¥¿¡¼¥ß¥Ê¥ë¥½¥Õ¥È¤Ç¤¹. X ¤ÎÉ¸½à¥¿¡¼¥ß¥Ê¥ë¥½
¥Õ¥È xterm ¤ËÆüËÜ¸ì¤ò¼è¤ê°·¤¦µ¡Ç½¤¬ÉÕ²Ã¤µ¤ì¤Æ¤¤¤Þ¤¹. xterm ¤Î¾å°Ì¸ß´¹
¤È¤Ê¤Ã¤Æ¤ª¤ê, ¥ª¥×¥·¥ç¥ó¤ÎÀßÄê¤äÁàºîÊýË¡¤Ï xterm ¤È¤Û¤È¤ó¤ÉÆ±¤¸¤Ç¤¹.
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï xterm ¥»¥­¥å¥ê¥Æ¥£¡¼¥Ñ¥Ã¥Á¤È16 ¿§¥Ñ¥Ã¥Á¤¬Åö¤¿¤Ã¤Æ¤¤
¤Þ¤¹.

¥É¥­¥å¥á¥ó¥È¤Ï man kterm ¤ª¤è¤Ó man xterm ¤ò»²¹Í¤Ë¤·¤Æ¤¯¤À¤µ¤¤.

%description -l pl
Pakiet kterm zawiera emulator terminala z japoñskim zestawem znaków
Kanji.

%description -l pt_BR
kterm é o Emulador de Terminal Kanji. Ele usa o conjunto de caracteres
Kanji ao invés do conjunto normal de inglês para aqueles que preferem
Kanji.

%description -l tr
kterm, Kanji uçbirim öykünümcüsüdür. Normal Ýngilizce karakter kümesi
yerine Kanji karakter kümesini kullanýr.

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
install -d $RPM_BUILD_ROOT%{_applnkdir}/Terminals

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Terminals/kterm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kterm
%{_libdir}/X11/app-defaults/KTerm
%{_mandir}/man1/kterm.1x*
%{_applnkdir}/Terminals/kterm.desktop
