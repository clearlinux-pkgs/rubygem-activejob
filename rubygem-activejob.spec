#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-activejob
Version  : 4.2.6
Release  : 7
URL      : https://rubygems.org/downloads/activejob-4.2.6.gem
Source0  : https://rubygems.org/downloads/activejob-4.2.6.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-globalid
BuildRequires : rubygem-rdoc

%description
# Active Job -- Make work happen later
Active Job is a framework for declaring jobs and making them run on a variety
of queueing backends. These jobs can be everything from regularly scheduled
clean-ups, to billing charges, to mailings. Anything that can be chopped up into
small units of work and run in parallel, really.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n activejob-4.2.6
gem spec %{SOURCE0} -l --ruby > rubygem-activejob.gemspec

%build
export LANG=C
gem build rubygem-activejob.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
activejob-4.2.6.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/activejob-4.2.6.gem
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/README.md
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/arguments.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/configured_job.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/enqueuing.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/execution.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/gem_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/logging.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/backburner_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/delayed_job_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/inline_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/qu_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/que_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/queue_classic_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/resque_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/sidekiq_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/sneakers_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/sucker_punch_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_adapters/test_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/queue_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/test_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/translation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/active_job/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/rails/generators/job/job_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/activejob-4.2.6/lib/rails/generators/job/templates/job.rb
/usr/lib64/ruby/gems/2.3.0/specifications/activejob-4.2.6.gemspec
