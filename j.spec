Summary:	j editor
Summary(pl.UTF-8):	Edytor j
Name:		j
Version:	0.19.0
Release:	1
Group:		Development/Tools
License:	GPL
# Source0-md5:	fe3c7f8466123713e33537a785305f4c
Source0:	http://dl.sourceforge.net/armedbear-j/%{name}-%{version}.tar.gz
URL:		http://armedbear-j.sourceforge.net/
Patch0:		%{name}-destdir.patch
BuildRequires:	jdk
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
j is a text editor written entirely in Java.

%description -l pl.UTF-8
j to edytor tekstu napisany całkowicie w Javie.

%prep
%setup -q
%patch0 -p1

%build
chmod 755 configure
chmod 755 mkinstalldirs
%configure2_13 				\
        --with-jdk=%{_libdir}/java	\
	--enable-jpty
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%doc doc/*
%dir %{_datadir}/j
%{_datadir}/j/themes
%{_datadir}/j/j.jar
