%define rbname bdb
%define version 0.6.6
%define release 2

Summary: An interface to Berkeley DB for Ruby
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPL
URL: https://moulon.inra.fr/ruby/bdb.html
Source0: ftp://moulon.inra.fr/pub/ruby/%{rbname}-%{version}.tar.bz2
Patch0:	ruby-bdb-dependency.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel
BuildRequires: db-devel

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
ruby extconf.rb --vendor
make
make test

%install
make install DESTDIR=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README.en examples docs Changes
%{ruby_vendorarchdir}/bdb.so




%changelog
* Mon May 07 2012 Crispin Boylan <crisb@mandriva.org> 0.6.6-1
+ Revision: 797311
- New release
- Fix for db5.3
- Rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-5mdv2011.0
+ Revision: 614723
- the mass rebuild of 2010.1 packages

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.6.5-4mdv2010.1
+ Revision: 498572
- build with db 4.8

* Sun Jan 24 2010 Rémy Clouard <shikamaru@mandriva.org> 0.6.5-3mdv2010.1
+ Revision: 495464
- rebuild for db4.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.5-2mdv2010.0
+ Revision: 442786
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.6.5-1mdv2009.1
+ Revision: 324515
- New upstream release

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.3-2mdv2009.0
+ Revision: 269231
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Pascal Terjan <pterjan@mandriva.org> 0.6.3-1mdv2009.0
+ Revision: 217779
- move to vendor dir
- build against 4.6

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - new version 0.6.3
    - rebuild for new binary libraries location

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 0.6.0-2mdv2008.0
+ Revision: 16989
- Use group Development/Ruby

