%define rbname bdb
%define version 0.6.0
%define release %mkrel 2

Summary: An interface to Berkeley DB for Ruby
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPL
URL: http://moulon.inra.fr/ruby/bdb.html
Source0: ftp://moulon.inra.fr/pub/ruby/%{rbname}-%{version}.tar.bz2
Patch0:	ruby-bdb-dependency.patch
BuildRequires: ruby-devel
BuildRequires: db4.2-devel

%description
This is an interface to Berkeley DB, it contains also an interface to
Berkeley DB XML.

%prep
%setup -q -n %{rbname}-%{version}
%patch0
for f in `find examples -name \*.rb`
do
	if head -n1 "$f" | grep '^#!' >/dev/null;
	then
		sed -i 's|/usr/local/bin|/usr/bin|' "$f"
		chmod 0755 "$f"
	else
		chmod 0644 "$f"
	fi
done

%build
ruby extconf.rb
make
make test

%install
make install DESTDIR=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README.en examples docs Changes
%{ruby_sitearchdir}/bdb.so


