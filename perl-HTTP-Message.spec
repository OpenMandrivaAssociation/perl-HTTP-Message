%define upstream_name    HTTP-Message
%define upstream_version 6.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Base class for Request/Response
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Raw::Zlib)
BuildRequires: perl(Encode)
BuildRequires: perl(Encode::Locale)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(IO::Compress::Bzip2)
BuildRequires: perl(IO::Compress::Deflate)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(IO::Uncompress::Bunzip2)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(IO::Uncompress::Inflate)
BuildRequires: perl(IO::Uncompress::RawInflate)
BuildRequires: perl(LWP::MediaTypes)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(MIME::QuotedPrint)
BuildRequires: perl(URI)
BuildRequires: perl-devel
BuildArch: noarch

%description
An 'HTTP::Config' object is a list of entries that can be matched against
request or request/response pairs. Its purpose is to hold configuration
data that can be looked up given a request or response object.

Each configuration entry is a hash. Some keys specify matching to occur
against attributes of request/response objects. Other keys can be used to
hold user data.

The following methods are provided:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Tue Feb 21 2012 Götz Waschk <waschk@mandriva.org> 6.30.0-1mdv2012.0
+ Revision: 778602
- update to new version 6.03

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-4
+ Revision: 765364
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-3
+ Revision: 763866
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-2
+ Revision: 763076
- rebuild

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.20.0-1
+ Revision: 664977
- import perl-HTTP-Message

