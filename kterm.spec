Summary:	A Kanji (Japanese character set) terminal emulator for X
Summary(de.UTF-8):	Kterm (Kanji-Terminal-Emulator)
Summary(es.UTF-8):	Kterm (Emulador de Terminal Kanji)
Summary(fr.UTF-8):	Kterm (Émulateur de terminal Kanji)
Summary(ja.UTF-8):	日本語の表示が可能な X 上のターミナルソフトです
Summary(pl.UTF-8):	Emulator terminala Kanji (z japońskimi znakami) dla X
Summary(pt_BR.UTF-8):	Kterm (Emulador de Terminal Kanji)
Summary(tr.UTF-8):	Kanji uçbirim öykünümcüsü
Name:		kterm
Version:	6.2.0
Release:	8
License:	distributable
Group:		X11/Applications
Source0:	ftp://ftp.sunet.se/pub/X11/R6contrib/applications/%{name}-%{version}.tar.gz
# Source0-md5:	9cc72841b50dfba92bce01dbbebf3039
Source1:	%{name}.desktop
Patch0:		%{name}-6.2.0-kbd.patch
Patch1:		%{name}-6.2.0-glibc.patch
Patch2:		%{name}-6.2.0-utmp98.patch
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%description -l de.UTF-8
kterm ist der Kanji-Terminal-Emulator. Statt des normalen englischen
Zeichensatzes arbeitet er mit dem japanischen Kanji-System.

%description -l es.UTF-8
kterm es el Emulador de Terminal Kanji. Usa el conjunto de caracteres
Kanji en lugar del conjunto normal de inglés para aquellos que
prefieran Kanji.

%description -l fr.UTF-8
kterm est l'émulateur de terminal Kanji. Il utilise les caractères
Kanji à la place des caractères français normaux.

%description -l ja.UTF-8
日本語の表示が可能な X 上のターミナルソフトです. X の標準ターミナルソ
フト xterm に日本語を取り扱う機能が付加されています. xterm の上位互換
となっており, オプションの設定や操作方法は xterm とほとんど同じです.
このパッケージには xterm セキュリティーパッチと16 色パッチが当たってい
ます.

ドキュメントは man kterm および man xterm を参考にしてください.

%description -l pl.UTF-8
Pakiet kterm zawiera emulator terminala z japońskim zestawem znaków
Kanji.

%description -l pt_BR.UTF-8
kterm é o Emulador de Terminal Kanji. Ele usa o conjunto de caracteres
Kanji ao invés do conjunto normal de inglês para aqueles que preferem
Kanji.

%description -l tr.UTF-8
kterm, Kanji uçbirim öykünümcüsüdür. Normal İngilizce karakter kümesi
yerine Kanji karakter kümesini kullanır.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} \
	CDEBUGFLAGS="%{rpmcflags} -fno-strength-reduce -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	XAPPLOADDIR=%{_appdefsdir} \
	MANDIR=%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kterm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kterm
%{_appdefsdir}/KTerm
%{_mandir}/man1/kterm.1x*
%{_desktopdir}/kterm.desktop
