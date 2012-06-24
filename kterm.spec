Summary:	A Kanji (Japanese character set) terminal emulator for X
Summary(de):	Kterm (Kanji-Terminal-Emulator)
Summary(es):	Kterm (Emulador de Terminal Kanji)
Summary(fr):	Kterm (�mulateur de terminal Kanji)
Summary(ja):	���ܸ��ɽ������ǽ�� X ��Υ����ߥʥ륽�եȤǤ�
Summary(pl):	Emulator terminala Kanji (z japo�skimi znakami) dla X
Summary(pt_BR):	Kterm (Emulador de Terminal Kanji)
Summary(tr):	Kanji u�birim �yk�n�mc�s�
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
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
Kanji en lugar del conjunto normal de ingl�s para aquellos que
prefieran Kanji.

%description -l fr
kterm est l'�mulateur de terminal Kanji. Il utilise les caract�res
Kanji � la place des caract�res fran�ais normaux.

%description -l ja
���ܸ��ɽ������ǽ�� X ��Υ����ߥʥ륽�եȤǤ�. X ��ɸ�ॿ���ߥʥ륽
�ե� xterm �����ܸ���갷����ǽ���ղä���Ƥ��ޤ�. xterm �ξ�̸ߴ�
�ȤʤäƤ���, ���ץ���������������ˡ�� xterm �ȤۤȤ��Ʊ���Ǥ�.
���Υѥå������ˤ� xterm �������ƥ����ѥå���16 ���ѥå��������äƤ�
�ޤ�.

�ɥ�����Ȥ� man kterm ����� man xterm �򻲹ͤˤ��Ƥ�������.

%description -l pl
Pakiet kterm zawiera emulator terminala z japo�skim zestawem znak�w
Kanji.

%description -l pt_BR
kterm � o Emulador de Terminal Kanji. Ele usa o conjunto de caracteres
Kanji ao inv�s do conjunto normal de ingl�s para aqueles que preferem
Kanji.

%description -l tr
kterm, Kanji u�birim �yk�n�mc�s�d�r. Normal �ngilizce karakter k�mesi
yerine Kanji karakter k�mesini kullan�r.

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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Terminals,%{_mandir},%{_bindir},%{_libdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT/usr/X11R6/man/* $RPM_BUILD_ROOT%{_mandir}
mv -f $RPM_BUILD_ROOT/usr/X11R6/bin/* $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT/usr/X11R6/lib/* $RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Terminals/kterm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kterm
%{_libdir}/X11/app-defaults/KTerm
%{_mandir}/man1/kterm.1x*
%{_applnkdir}/Terminals/kterm.desktop
