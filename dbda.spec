Name:           dbda
Version:        1.0
Release:        1%{?dist}
Summary:        The "dbda repo" program from GNU

License:        GPLv3+
URL:            http://ftp.gnu.org/gnu/%{name}
Source0:        ./repo

#BuildRequires: gettext

Requires(post): info
Requires(preun): info

%description
The "dbda" program package
