Summary:	EMail index and search tool
Name:		mairix
Version:	0.15.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.rpcurnow.force9.co.uk/mairix/%{name}-%{version}.tar.gz
# Source0-md5:	cab61e4e95184541e6b7b4f67dfca3cc
URL:		http://www.rpcurnow.force9.co.uk/mairix/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mairix is a program for indexing and searching email messages stored in 
Maildir, MH or mbox folders.

Some features:

* Indexing is fast. It runs incrementally on new messages - any 
  particular message only gets scanned once in the lifetime of the 
  index file.
* The search mode populates a "virtual" maildir (or MH) folder with 
  symlinks which point to the real messages. This folder can be opened 
	as usual in your mail program. (Note, if messages are in mbox folders, 
	copies are made. Similarly if the virtual folder has mbox format, it 
	is filled with copies of the matched messages.)
* The search mode is very fast.
* Indexing and searching works on the basis of words. The index file 
  tabulates which words occur in which parts (particular headers + body) 
	of which messages. `

%prep
%setup -q 

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
./configure --prefix=%{_prefix} --mandir=%{_mandir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README dotmairixrc.eg mairix.txt
%attr(755,root,root) %{_bindir}/*
#%{_mandir}/*/*
