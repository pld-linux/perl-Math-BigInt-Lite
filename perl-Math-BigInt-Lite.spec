#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-Lite
Summary:	Math::BigInt::Lite - what BigInts are before they become big
Summary(pl.UTF-8):	Math::BigInt::Lite - czym były BigInty zanim stały się duże
Name:		perl-Math-BigInt-Lite
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaf0d0f526b355d525e7f2857b62be7e
URL:		http://search.cpan.org/dist/Math-BigInt-Lite/
BuildRequires:	perl-Math-BigInt >= 1.94
BuildRequires:	perl-Math-BigRat >= 0.19
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.52
%endif
Requires:	perl-Math-BigInt >= 1.94
Requires:	perl-Math-BigRat >= 0.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt is not very good suited to work with small (read: typical
less than 10 digits) numbers, since it has a quite high per-operation
overhead and is thus too slow. But for some simple applications, you
don't need rounding, infinity nor NaN handling, and yet want fast
speed for small numbers without the risk of overflowing. This is were
Math::BigInt::Lite comes into play.

Math::BigInt::Lite objects should behave in every way like
Math::BigInt objects, that is apart from the different label, you
should not be able to tell the difference. Since Math::BigInt::Lite is
designed with speed in mind, there are certain limitations build-in.
In praxis, however, you will not feel them, because everytime
something gets to big to pass as Lite (literally), it will upgrade the
objects and operation in question to Math::BigInt.

%description -l pl.UTF-8
Moduł Math::BigInt nie jest dobrze dopasowany do pracy z małymi (tzn.
najczęściej poniżej 10 cyfr) liczbami, ponieważ ma zbyt duży narzut na
każdą operację, przez co jest zbyt wolny. Ale dla niektórych prostych
aplikacji nie potrzebne jest zaokrąglanie, obsługa nieskończoności czy
NaN, za to potrzebna jest szybkość obliczeń na małych liczbach bez
ryzyka przepełnienia. Jest to sytuacja, dla której został stworzony
Math::BigInt::Lite.

Obiekty Math::BigInt::Lite powinny zachowywać się tak samo jak obiekty
Math::BigInt - bez widocznej różnicy oprócz nazwy. Ponieważ moduł
Math::BigInt::Lite jest zaprojektowany z myślą o szybkości, ma pewne
ograniczenia. W praktyce nie powinniśmy ich odczuć, ponieważ jeśli
tylko coś staje się zbyt duże do przekazania jako Lite, obiekt
zostanie powiększony, a operacja przeprowadzona przez Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{_mandir}/man3/Math::BigInt::Lite.3pm*
