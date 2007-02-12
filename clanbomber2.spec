Summary:	ClanBomber2 a network compatible version of ClanBomber
Summary(pl.UTF-8):	ClanBomber2, sieciowa wersja ClanBombera
Name:		clanbomber2
Version:	0.9
Release:	0.3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/clanbomber/%{name}-%{version}.tar.gz
# Source0-md5:	eb9449e2ddffd5d1874a4d34fd289ae3
Source1:	%{name}.desktop
Source2:	clanbomber.png
URL:		http://clanbomber.sourceforge.net/
BuildRequires:	DirectFB-devel >= 0.9.18
BuildRequires:	FusionSound-devel >= 0.9.19
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	FusionSound >= 0.9.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClanBomber2 is very nice and playable Bomberman/Dynablaster clone. It
has network and multiplayer support. You must have try it! :-)

%description -l pl.UTF-8
ClanBomber2 to bardzo fajna i wciągająca gierka, zbliżona do
Bombermana/Dynablastera. Posiada wsparcie do gry sieciowej oraz można
w nią grać w kilku. Koniecznie musisz ją wypróbować!

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog QUOTES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
