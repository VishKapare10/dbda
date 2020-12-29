Name:           dbda
Version:        3.0
Release:        1%{?dist}
Summary:        A test script

Group:          Utilities
License:        GPL
URL:            http://oracle-base.com/articles/linux/linux-build-simple-rpm-packages.php
Source0:        dbda-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


#BuildRequires:
#Requires:

%description
A test script inside a simple RPM package


#%prep
#%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/dbda
install dbda/* $RPM_BUILD_ROOT/opt/dbda/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /opt/dbda
%defattr(-,root,root,-)
/opt/dbda/*

%post
chmod 755 -R /opt/dbda
