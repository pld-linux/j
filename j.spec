Summary:	j editor
Summary(pl):	Edytof j
Name:		j
Version:	0.16.3
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	http://cesnet.dl.sourceforge.net/armedbeer-j/%{name}-%{version}.tar.gz
Patch0:		%{name}-destdir.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
j editor

%description -l pl
Edytor j

%prep
%setup -q
%patch0 -p1

%build
chmod 755 configure
chmod 755 mkinstalldirs
%configure2_13 				\
        --with-jdk=/usr/lib/java	\
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
%{_datadir}/j/themes/*
%{_datadir}/j/j.jar
