Summary:	Simple DirectMedia Layer 3 - network
Summary(pl.UTF-8):	Biblioteka obsługi sieci w SDL3
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer 3 - Biblioteca de rede portável
Name:		SDL3_net
Version:	3.2.0
Release:	1
License:	Zlib-like
Group:		Libraries
#Source0Download: https://github.com/libsdl-org/SDL_net/releases
Source0:	https://github.com/libsdl-org/SDL_net/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d2a5caa432d8620caa244285000aa2ee
URL:		https://github.com/libsdl-org/SDL_net
BuildRequires:	SDL3-devel >= 3.0.0
BuildRequires:	cmake >= 3.16
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	SDL3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an example portable network library for use with SDL3. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl.UTF-8
Przykładowa biblioteka obsługi sieci korzystająca z SDL3.

%description -l pt_BR.UTF-8
Esta é uma biblioteca portável de rede para uso com o SDL3.

%package devel
Summary:	Header files and more to develop SDL3_net applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL3_net
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL3_net
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL3-devel >= 3.0.0

%description devel
This package contains the headers that programmers will need to
develop applications which will use SDL3_net.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowepotzrebne przy rozwijania aplikacji
używających SDL3_net.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL3_net.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{_libdir}/libSDL3_net.so.*.*.*
%ghost %{_libdir}/libSDL3_net.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libSDL3_net.so
%{_includedir}/SDL3_net
%{_pkgconfigdir}/sdl3-net.pc
%{_libdir}/cmake/SDL3_net
