Summary:	EMail index and search tool
Summary(hu.UTF-8):	EMail indexelő és kereső eszköz
Summary(pl.UTF-8):	Narzędzie do indeksowania i przeszukiwania poczty elektronicznej
Name:		mairix
Version:	0.21
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/mairix/%{name}-%{version}.tar.gz
# Source0-md5:	821619895931711c370f51f3442a0ded
Patch0:		%{name}-claws-support.patch
URL:		http://www.rc0.org.uk/mairix
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mairix is a program for indexing and searching email messages stored
in Maildir, MH or mbox folders.

Some features:
- Indexing is fast. It runs incrementally on new messages - any
  particular message only gets scanned once in the lifetime of the index
  file.
- The search mode populates a "virtual" maildir (or MH) folder with
  symlinks which point to the real messages. This folder can be opened
  as usual in your mail program. (Note, if messages are in mbox folders,
  copies are made. Similarly if the virtual folder has mbox format, it
  is filled with copies of the matched messages.)
- The search mode is very fast.
- Indexing and searching works on the basis of words. The index file
  tabulates which words occur in which parts (particular headers + body)
  of which messages.

%description -l hu.UTF-8
mairix egy program, amellyel Maildir, MH vagy mbox mappákban tárolt
email-jeid indexelheted és keresheted.

Néhány lehetőség:
- Az indexelés gyors. Inkrementálisan fut az új leveleken - minden
  üzenetet az élete alatt csak egyszer vizsgál át.
- A keresési mód egy "virtuális" maildir-t (vagy MH-t) hoz létre
  szimbolikus linkekkel, amelyek a valódi üzenetre mutatnak. Ez a
  könyvtár általában megnyitható az email programoddal. (Figyelj arra,
  hogy ha az üzenetek mbox könyvtárakban vannak, másolatok készülnek.
  Hasonlóan, ha a virtuális könyvtár mbox formátumú, az egyező üzenetek
  másolataival töltődik fel.)
- A keresési mód nagyon gyors.
- Az indexelés és a keresés szó-alapon működik Az index file
  tabulálja, hogy melyik szó melyik üzenet mely részével (fejlécek +
  body) egyezik.

%description -l pl.UTF-8
mairix to program do indeksowania i przeszukiwania poczty
elektronicznej zapisanej w folderach typu Maildir, MH lub mbox.

Niektóre możliwości:
- Indeksowanie jest szybkie - program działa przyrostowo na nowych
  wiadomościach, a każda wiadomość jest skanowana tylko raz w ramach
  czasu życia pliku indeksu.
- Tryb przeszukiwania wypełnia "wirtualny" folder maildir (lub MH)
  dowiązaniami wskazującymi na właściwe wiadomości. Folder ten może być
  normalnie otwierany w programie pocztowym. (Uwaga: jeśli wiadomości są
  w folderach mbox, tworzone są kopie. Podobnie jeśli wirtualny folder
  ma format mbox, jest wypełniany kopiami pasujących wiadomości).
- Tryb przeszukiwania jest bardzo szybki.
- Indeksowanie i przeszukiwanie działa w oparciu o słowa. Plik indeksu
  tablicuje które słowa występują w których częściach (konkretnych
  nagłówkach i ciele) których wiadomości.

%prep
%setup -q
%patch -P0 -p1

%build
./configure \
	--mandir=%{_mandir} \
	--prefix=%{_prefix}

%{__make}

for i in README NEWS ;do
	mv dfasyn/$i $i.dfasyn
done

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install dfasyn/dfasyn $RPM_BUILD_ROOT%{_bindir}
install mairix.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mairixrc.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dotmairixrc.eg ACKNOWLEDGEMENTS  README.dfasyn NEWS.dfasyn
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
