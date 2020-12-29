Name:       dbda
Version:    30
Release:    1
Summary:    Most simple RPM package
License:    FIXME

URL:        http://ftp.gnu.org/gnu/%{name}
Source0:    ./dbda.tar.gz

%description
This is my first RPM package.

%prep

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
