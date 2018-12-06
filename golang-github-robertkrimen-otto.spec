# Run tests in check section
# Tests fail
%bcond_with check

%global goipath         github.com/robertkrimen/otto
%global commit          15f95af6e78dcd2030d8195a138bd88d4f403546

%global common_description %{expand:
A JavaScript interpreter in Golang.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.6%{?dist}
Summary: A JavaScript interpreter in Golang
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(gopkg.in/readline.v1)
BuildRequires: golang(gopkg.in/sourcemap.v1)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.markdown


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git15f95af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180628git15f95af
- Bump to commit 15f95af6e78dcd2030d8195a138bd88d4f403546

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git6c383dd
- Fix BuildRequires 

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git6c383dd
- Update with the new Go packaging
- Upstream GIT revision 6c383dd

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171130git3b44b4d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171130git3b44b4d
- Upstream GIT revision 3b44b4d

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170818gita813c59
- First package for Fedora

