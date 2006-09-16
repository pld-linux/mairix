Summary:	EMail index and search tool
Summary(pl):	Narzêdzie do indeksowania i przeszukiwania poczty elektronicznej
Name:		mairix
Version:	0.19
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/mairix/%{name}-%{version}.tar.gz
# Source0-md5:	9b384a0fa3431868d5198a7f1882ee69
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

%description -l pl
mairix to program do indeksowania i przeszukiwania poczty
elektronicznej zapisanej w folderach typu Maildir, MH lub mbox.

Niektóre mo¿liwo¶ci:
- Indeksowanie jest szybkie - program dzia³a przyrostowo na nowych
  wiadomo¶ciach, a ka¿da wiadomo¶æ jest skanowana tylko raz w ramach
  czasu ¿ycia pliku indeksu.
- Tryb przeszukiwania wype³nia "wirtualny" folder maildir (lub MH)
  dowi±zaniami wskazuj±cymi na w³a¶ciwe wiadomo¶ci. Folder ten mo¿e byæ
  normalnie otwierany w programie pocztowym. (Uwaga: je¶li wiadomo¶ci s±
  w folderach mbox, tworzone s± kopie. Podobnie je¶li wirtualny folder
  ma format mbox, jest wype³niany kopiami pasuj±cych wiadomo¶ci).
- Tryb przeszukiwania jest bardzo szybki.
- Indeksowanie i przeszukiwanie dzia³a w oparciu o s³owa. Plik indeksu
  tablicuje które s³owa wystêpuj± w których czê¶ciach (konkretnych
  nag³ówkach i ciele) których wiadomo¶ci.

%prep
%setup -q

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
