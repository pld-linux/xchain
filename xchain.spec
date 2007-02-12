Summary:	A strategy game for 2-4 players
Summary(pl.UTF-8):	Gra strategiczna dla 2-4 graczy
Name:		xchain
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.debian.org/debian/pool/main/x/xchain/%{name}_%{version}.orig.tar.gz
# Source0-md5:	4b4d5912f0fcd6b8f43426ab0a5cc4f3
Source1:	%{name}.desktop
Source2:	%{name}.png
Requires:	/usr/bin/wish
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Chain Reaction is a classic strategy game for 2-4 players. Players
take turns to place tokens on an 8x8 board. When a square exceeds it's
maximum value, it explodes, setting off the surrounding squares.

%description -l pl.UTF-8
Chain Reaction to klasyczna gra strategiczna dla 2-4 graczy. Gracze po
kolei umieszczają elementy na planszy 8x8. Kiedy kwadrat przekroczy
wartość maksymalną, eksploduje, zmieniając sąsiednie kwadraty.

%prep
%setup -q

gunzip xchain.6.gz

%build
%{__cc} %{rpmcflags} %{rpmldflags} xchain.c -o xchain

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir}}

install xchain $RPM_BUILD_ROOT%{_bindir}
install xchain.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
