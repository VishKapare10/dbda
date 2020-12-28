Name:       dbda
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
Source0:    /home/runner/work/dbda/dbda/dbda.tar.gz

%build
cat > dbda.sh <<EOF
#!/usr/bin/bash
echo hello dbda! 
EOF


%changelog
# let's skip this for now
