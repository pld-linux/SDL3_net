Summary:	Simple DirectMedia Layer 2 - network
Summary(pl.UTF-8):	Biblioteka obsługi sieci w SDL2
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer 2 - Biblioteca de rede portável
Name:		SDL2_net
Version:	2.4.0
Release:	1
License:	Zlib-like
Group:		Libraries
#Source0Download: https://github.com/libsdl-org/SDL_net/releases
Source0:	https://github.com/libsdl-org/SDL_net/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5475106690595d03f32399799890dbb6
URL:		https://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL2-devel >= 2.0.4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.0
Requires:	SDL2 >= 2.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an example portable network library for use with SDL2. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl.UTF-8
Przykładowa biblioteka obsługi sieci korzystająca z SDL2.

%description -l pt_BR.UTF-8
Esta é uma biblioteca portável de rede para uso com o SDL2.

%package devel
Summary:	Header files and more to develop SDL2_net applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL2_net
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL2_net
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel >= 2.0.4

%description devel
This package contains the headers that programmers will need to
develop applications which will use SDL2_net.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowepotzrebne przy rozwijania aplikacji
używających SDL2_net.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL2_net.

%package static
Summary:	Static SDL2_net libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL2_net
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento utilizando a SDL2_net
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL2_net libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL2_net.

%description static -l pt_BR.UTF-8
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
SDL2_net.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{_libdir}/libSDL2_net-2.0.so.*.*.*
%ghost %{_libdir}/libSDL2_net-2.0.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libSDL2_net.so
%{_includedir}/SDL2/SDL_net.h
%{_pkgconfigdir}/SDL2_net.pc
%{_libdir}/cmake/SDL2_net

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2_net.a
