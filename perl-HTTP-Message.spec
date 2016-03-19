%define modname	HTTP-Message
%define modver	6.03

Summary:	Base class for Request/Response
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Compress::Raw::Zlib)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Encode::Locale)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(IO::Compress::Bzip2)
BuildRequires:	perl(IO::Compress::Deflate)
BuildRequires:	perl(IO::Compress::Gzip)
BuildRequires:	perl(IO::Uncompress::Bunzip2)
BuildRequires:	perl(IO::Uncompress::Gunzip)
BuildRequires:	perl(IO::Uncompress::Inflate)
BuildRequires:	perl(IO::Uncompress::RawInflate)
BuildRequires:	perl(LWP::MediaTypes)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(MIME::QuotedPrint)
BuildRequires:	perl(URI)
BuildRequires:	perl-devel

%description
An 'HTTP::Config' object is a list of entries that can be matched against
request or request/response pairs. Its purpose is to hold configuration
data that can be looked up given a request or response object.

Each configuration entry is a hash. Some keys specify matching to occur
against attributes of request/response objects. Other keys can be used to
hold user data.

The following methods are provided:

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*

