#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigInt-Lite
Summary:	Math::BigInt::Lite - what BigInts are before they become big
Summary(pl):	Math::BigInt::Lite - czym by³y BigInty zanim sta³y siê du¿e
Name:		perl-Math-BigInt-Lite
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	253dafb83e3317cb6118b2ac6bd23577
Patch0:		%{name}-test.patch
BuildRequires:	perl-Math-BigInt >= 1.57
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.57
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt is not very good suited to work with small (read: typical
less than 10 digits) numbers, since it has a quite high per-operation
overhead and is thus too slow. But for some simple applications, you
don't need rounding, infinity nor NaN handling, and yet want fast speed
for small numbers without the risk of overflowing. This is were
Math::BigInt::Lite comes into play.

Math::BigInt::Lite objects should behave in every way like
Math::BigInt objects, that is apart from the different label, you
should not be able to tell the difference. Since Math::BigInt::Lite is
designed with speed in mind, there are certain limitations build-in.
In praxis, however, you will not feel them, because everytime
something gets to big to pass as Lite (literally), it will upgrade the
objects and operation in question to Math::BigInt.

%description -l pl
Modu³ Math::BigInt nie jest dobrze dopasowany do pracy z ma³ymi (tzn.
najczê¶ciej poni¿ej 10 cyfr) liczbami, poniewa¿ ma zbyt du¿y narzut na
ka¿d± oparacjê, przez co jest zbyt wolny. Ale dla niektórych prostych
aplikacji nie potrzebne jest zaokr±glanie, obs³uga nieskoñczono¶ci czy
NaN, za to potrzebna jest szybko¶æ obliczeñ na ma³ych liczbach bez
ryzyka przepe³nienia. Jest to sytuacja, dla której zosta³ stworzony
Math::BigInt::Lite.

Obiekty Math::BigInt::Lite powinny zachowywaæ siê tak samo jak obiekty
Math::BigInt - bez widocznej ró¿nicy oprócz nazwy. Poniewa¿ modu³
Math::BigInt::Lite jest zaprojektowany z my¶l± o szybko¶ci, ma pewne
ograniczenia. W praktyce nie powinni¶my ich odczuæ, poniewa¿ je¶li
tylko co¶ staje siê zbyt du¿e do przekazania jako Lite, obiekt
zostanie powiêkszony, a operacja przeprowadzona przez Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# sqrt(+inf) == inf, not NaN
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES LICENSE NEW README TODO
%{perl_vendorlib}/Math/BigInt/Lite.pm
%{_mandir}/man3/*
