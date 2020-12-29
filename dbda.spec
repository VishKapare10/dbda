Name:       dbda
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

URL:        http://ftp.gnu.org/gnu/%{name}
Source0:    ./dbda.tar.gz

%description
This is my first RPM package.

%prep

#%build
#cat > dbda.sh <<EOF
#!/usr/bin/bash
#echo hello dbda!
#EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 dbda/code/* %{buildroot}/usr/bin/

%files
/usr/bin/*

#%changelog
