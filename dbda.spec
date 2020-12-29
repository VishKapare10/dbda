Name:       dbda
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

URL:            http://ftp.gnu.org/gnu/%{name}
Source0:        ./dbda.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A test script inside a simple RPM package

#%prep
# we have no source, so nothing here

#%build
#cat > dbda.sh <<EOF
##!/usr/bin/bash
#echo hello dbda!
#EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/dbda
install dbda/code/* $RPM_BUILD_ROOT/opt/dbda/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /opt/dbda
%defattr(-,root,root,-)
/opt/dbda/*

%post
chmod 755 -R /opt/dbda
