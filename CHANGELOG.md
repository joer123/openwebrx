**1.2.88**
- Further improved noise reduction algorithm.
- Added separate WMBus decoder using rtl-433.
- Switched rtl-433 decoder to CF32 IQ format.
- Removed AGC from the rtl-433 decoder input.
- Fixed CW skimmer window not showing up.

**1.2.87**
- Added file size display to the file browser.
- Added configurable limit of clients per IP address.
- Added configurable hang time to audio recording.
- Reduced squelch hang time back, by public request.
- Widened noise reduction control range to 20dB.
- Improved noise reduction algorithm.
- Improved SNR computation.

**1.2.86**
- Added SNR-based "smart squelch" to audio recorder.
- Set background recording squelch to around +20dB.
- Increased default squelch hang time to one second.
- Disabled awkward "camera control" in Google Maps.
- Removed NOAA-18 support (satellite decommissioned).
- Added logo display to HDRadio stations.
- Added 'aprs-symbols' as requirement to receive APRS.

**1.2.85**
- Added configurable DAB output rate.
- Added configurable AGC to SSB analog modes.
- Added LAGGY and MID AGC modes, useful for SSB.
- Changed SSB bandpass filter to 150..2750Hz.

**1.2.84**
- Enabled ADSB updates via MQTT.
- Added hang time to squelch to avoid dropouts.
- Added squelch to background audio recorder.
- Background recording squelch set via Setings.

**1.2.83**
- Added configurable image compression (Jacob Morris).
- Added SoapySDDC RX-888 SDR source (Lax Telcel).
- Added more Yaesu radios to APRS (Geoffrey Phillips).
- Added Kenwood TH-D75 to APRS (Geoffrey Phillips).

**1.2.82**
- Added check for a specific end-of-fax-page marker.
- Set default maximum fax page length to 1500.

**1.2.81**
- Now truncating FAX images as transmission ends.
- Now saving SSTV images if at least half is received.
- Added function to adjust image size when closing image.
- Added configurable minimum fax length parameter.
- Fixed error when entering profile with default digital mode.
- Fixed noise reduction level display.
- Refactored data recording.

**1.2.80**
- Added server-side background audio recording to MP3.
- Audio recordings are shown at the "Files" page.
- Audio recorder requires Linux "lame" package.
- Sorted contents of "Files" page by creation time.
- Sorted services in background decoding settings.
- Moved mode requirements check from client to server.
- Retaining underlying modulation on mode changes.
- Fixed frequency scale background in default theme.
- Fixed missing math import in toolbox.py.
- Fixed typo in Northwood bookmarks.
- Randomized web user agent string.
- Updated NRSC5 Python library.

**1.2.79**
- Added configurable fax page length limit.
- Added OWRX+ version to RepeaterBook agent string.
- Shrunk SDRPlay rfgain_sel range to 0..27.
- Refactored and improved web agents.
- Added newer Yaesu radios to APRS (Geoffrey Phillips).
- Fixed Leaflet geodesic line bugs (Stanislav Lechev).

**1.2.78**
- Randomized web refresh times for repeaters and receivers.
- Introduced web refresh cutoff after several failures.
- Added server lookup from callsigns to countries.
- Added server lookup from MMSIs to countries.
- Added more profiles to the default RTLSDR device.
- Fixed NumericMapping bug.

**1.2.77**
- Refactored web data sources (EIBI, receivers, repeaters).
- Fixed RepeaterBook updates to happen daily.
- Fixed KiwiSDR receiver database updates.
- Added aircraft and country lookup by ICAO ID (from TAR1090).
- Added country and its flag to aircraft map bubbles.
- Added OpenWebRX uptime display to Settings page.
- Added Linux uptime display to Settings page.
- Added receivers database update time to Settings page.

**1.2.76**
- Refactored SSTV decoder code.
- Eliminated FFTW3 race condition in SSTV decoder.
- Disabled AVT-90 SSTV mode due to quality concerns.
- Fixed Scottie DX VIS code.
- Improved CW skimmer sensitivity.
- Not clearing CW skimmer when frequency changes.
- Settings page shows EIBI schedule download time.
- Settings page shows repeaters list download time.
- Using degree sign for temperatures on the map.

**1.2.75**
- Added profile-specific transceiver rig control setting.
- Added CLEAR button to CW skimmer.
- Replaced ascent/descent symbols Chrome turned into emojis.
- Removed backslash before underscore in 'freedv_rx'.
- Now loading UI and audio settings separately.
- Removed some FT8 debug messages.
- Silenced CW skimmer audio.

**1.2.74**
- Added CWSkimmer decoder using csdr-cwskimmer tool.
- Added UI.tuneBookmark(), UI.toggleScanner().
- Fixed FLEX decoder to parse multiple capcodes.
- Fixed several scanner bugs.
- No longer translating EIBI CW bookmarks 800Hz down.

**1.2.73**
- Added frequency to recorded MP3 filenames.
- Added 800Hz to newly created CW bookmarks.
- Refactored frequency and modulation UI code.
- Accounted for ACARS altitudes set to "ground".
- Stripped whitespace from input strings.
- Fixed SSL on newer Python3 versions.

**1.2.72**
- Added underlying modulation to bookmarks.
- Added sanitizing bookmark contents.
- Added bias-tee support for rtl_tcp [jeskko].
- Added dependency on python3-distutils-extra.
- Fixed Chrome bug opening "Settings" section.
- Refactored bookmark editing mechanism.

**1.2.71**
- Added PD50, PD90, PD120, PD160, PD180, PD240, PD290 SSTV modes.
- Added Wraase SC2-30, SC2-60, SC2-120 SSTV modes.
- Added Scottie 3 and Scottie 4 SSTV modes (please test).
- Added Martin 3 and Martin 4 SSTV modes (please test).
- Added Robot 12 and Robot 24 SSTV modes (please test).
- Added AVT-90 SSTV mode.
- Added "Settings | General | External links" section.
- Fixed FT8 call distances not hiding on Leaflet maps.
- [ENTER] toggles receiver panel, [L] toggles log/chat.
- Now marking SSTV BMPs with 0x73 at offset 7.

**1.2.70**
- Fixed flood of broken pipe errors when client disconnects.
- Added ability to control external transceiver rigs.
- Added geodesic call lines and distance to Leaflet maps.
- Added tuning by squelch with [[]/[]] keys.
- Squelch control now achieved with [{]/[}] keys.
- Tuning step control done with [SHIFT]+[LEFT]/[RIGHT] keys.
- Updated keyboard shortcuts help panel.

**1.2.69**
- Added [ALT]+[UP]/[DOWN] for volume control on MacOS.
- Fixed an exception when any of the markers fail to load.
- Fixed call arrows remaining after locator display disabled.
- Fixed Chrome showing empty "Settings" UI section.
- Fixed callsign linkification in FT8/FT4 modes.
- Blocked keyboard shortcuts until settings are loaded.
- Sorted digital modes inside combo box (by Richard Murnane).

**1.2.68**
- Added map display of completed FT8 calls.
- Added config to limit the number of shown calls.
- Added config to limit retention time of shown calls.
- Fixed HTTPS support by catching SSL-specific exception.
- Fixed and optimized map-related JavaScript code.
- [PgUp]/[PgDown] keys change center frequency, if allowed.

**1.2.67**
- Added keyboard shortcuts (press [?] for help).
- Added range check to the FFT overlap parameter.

**1.2.66**
- Added bookmark option to enable/disable scanning.
- SSB, CW, AM, SAM, and NFM bookmarks are scanned by default.
- Fixed importing local bookmarks missing new fields.
- Fixed crashes when disconnecting clients.

**1.2.65**
- Added MQTT reporting of server startup / shutdown.
- Added MQTT reporting of client connections.
- Added MQTT reporting of chat messages.
- Added reporting for raw AX25 data [rassware].
- Stated max panorama / avatar image sizes [jordank195].
- Made "Files" page compatible with reverse proxy [413137366].

**1.2.64**
- Added support for HDRadio (NRSC5) digital FM radio.
- Now requiring CSDR version 0.18.24.
- Fixed some HFDL bookmarks.

**1.2.63**
- Fixed crash in the FLEX decoder.
- Fixed crash in the EAS decoder.
- Fixed rounding error when editing bookmarks.
- Fixed suffix when entering bookmark in Hz.
- Now defaulting new bookmarks to kHz.
- Reduced number of GPS updates and logging.

**1.2.62**
- Added 24kHz DATA mode for the starving masses.
- Added optional descriptions to bookmarks.
- Added station descriptions to EIBI bookmarks.
- Added repeater descriptions to RepeaterBook bookmarks.
- Changed some messages from DEBUG to INFO and ERROR.
- Renamed Zoran's theme to Blue Ocean.
- Polling GPS every 5 minutes now.

**1.2.61**
- Added Multimon-based EAS decoder by Matthew McDougal.
- Added separate, selectable bandplans for ITU regions.
- Added Eclipse waterfall theme by Dimitar Milkov.
- Added HFGCS, MARS, and CAF aviation bookmarks.
- Sorting bands by low_band for in-order rendering.

**1.2.60**
- Added optional band plan display above bookmarks.
- Fixed reference to soapyMiri driver.
- Switched aviation emergency frequencies to AM.
- Added one more aviation emergency frequency.
- Updated band names.

**1.2.59**
- Added optional receiver location updates via GPSD.
- Added copyright-free Mirics driver for SDRPlay and clones.
- Fixed OpenWebRX startup failure if MQTT connection fails.
- Volume control is now logarithmic, in -55db to +5db range.
- Removing repeaters.json when receiver moves by >10km.
- Added Aircraft Emergency Frequency bookmark.

**1.2.58**
- Added MQTT reporting of SDR profile and status changes.
- SDR changes reported via "openwebrx/RX" MQTT topic.
- Decodes reported via "openwebrx/<mode>" MQTT topics.
- Fixed background PAGE decoding with a workaround.
- Fixed Selector API errors when withSquelch=False.
- Switched PAGE decoders to millisecond timestamps.
- Switched PAGE and ISM file recording to JSON.
- Separated FLEX baud rate from channel number.
- Made relevant PAGE JSON fields integer.
- Cleaned up TextParser, PAGE, and ISM decoders.
- Added debug code to print module chains.

**1.2.57**
- Added user-selectable waterfall color themes.
- Added initial data to all aircraft MQTT reports.
- Added current frequency to all reported JSON data.
- Stopped adding secondary offset if there is no selector.
- Switched all JSON timestamps to milliseconds.
- Moved waterfall functions outside openwebrx.js.
- Moved UI and utility functions outside openwebrx.js.
- Refactored aircraft mode parsers.

**1.2.56**
- Added character set setting for the pager messages.
- Added more default profiles to a new SDRPlay device.
- Added bookmarks for MURS frequencies.
- Fixed HTML formatting issue in the Feature Report.
- Fixed exception trying to report filtered pager messages.
- Moved Multimon, DumpHFDL, DumpVDL2 decoders to ExecModule.
- Made receiver location available to plugins via Utils.js.
- Updated remaining Feature Report instructions.
- Swapped opacity and theme chooser icons.

**1.2.55**
- Refactored and greatly improved CW decoder.
- Added NAVTEX decoder and background service.
- Added LW/MW band and NAVTEX frequencies to the bandplan.
- Added MQTT reports for APRS, AIS, PAGE, ISM modes.
- Added MQTT reports for HFDL, VDL2, ACARS, DSC modes.
- [jketterl] Added MQTT reporting.
- [jketterl] Improved PlutoSDR source.

**1.2.54**
- Made FT8/JS8/WSPR/etc. messages show in monospace font.
- Added ability to click on FT8/JS8/etc. callsigns.
- Added columns to the time displays.
- Fixed locators not aging when updated.
- Fixed race condition between move-profile requests.
- Now defaulting all new profile fields to kHz.

**1.2.53**
- Added ability to reorder profiles in the Settings.
- Added option to ignore incomplete DSC messages.
- Improved background service output to files.
- Improved preamble detection in CCIR493.
- Relaxed DSC FORMAT/EOS field requirements.
- Fixed profile reordering when a source is reenabled.
- Fixed wxsat frequencies in bands.json.

**1.2.52**
- Added MID codes for coastal stations, by continent.
- Added secondary selector offset to the dial frequency.
- Fixed dial frequency updates when secondary FFT clicked.
- Fixed repeated secondary demodulator creation.
- Improved CCIR493 and SITORB decoders.
- Printing valid DSC messages as INFO, errors as DEBUG.
- Not killing SatDump, will quit on its own.

**1.2.51**
- Background DSC decoding now works.
- Added DSC display of timestamps and frequencies.
- Added preliminary SatDump support (experts only!)
- Removed 'apt install' lines from feature instructions.
- Slightly optimized ExecModule operation.
- Improved DSC reception quality.
- Allowed dash in modulation names.

**1.2.50**
- Added DSC decoder and bookmarks.
- Rolled wide-band ISM back to 250kHz with bandpass.
- Limited scanner to LSB, USB, CW, AM, SAM, and NFM modes.
- Clarified installation instructions for some features.
- Now clearing FAILED device status when disabling device.
- Now resetting CW decoder state on frequency changes.
- Updated feature descriptions in feature.py.
- Moved all linkification to Utils.js.
- Fixed APRS rain reports.

**1.2.49**
- Added optimizations to DAB processing made by Jakob.
- Removed bandpass filters from ADS-B and ISM modes.
- Increased ISM bandwidth to 1.2Msps.
- Coloring ground-to-air messages black.

**1.2.48**
- Added chat nicknames to the clients display.
- Fixed DAB support by adding missing Dablin class.
- Fixed secondary waterfall height in SSTV and FAX modes.
- Allowed full range of SDRPlay samplerates.
- Allowed full range of HackRF samplerates.
- Extended default samplerate range to 30Msps.
- Improved RDS information display.
- Switched RDS to ExecModule (YOU HAVE TO UPDATE REDSEA).
- Switched RDS to the original, optimized parser.

**1.2.47**
- Merged changes from Jakob Ketterl's original development branch.
- Switched to updated CSDR, PyCSDR, OWRX Connector packages.
- Fixed WSJT out-of-band reports showing as "null" on the map.
- Fixed top bar icons disappearing on mobile devices.
- Fixed compatibility with Python 3.12+.
- Fixed orientation of some APRS symbols.
- Removed separate RDS decoder (now part of WFM).
- [jketterl] Added support for DAB radio via Dablin (untested in OWRX+).
- [jketterl] Added always-on RDS decoder in WFM mode.
- [jketterl] Added checks for valid source bandwidths.
- [jketterl] Added Afedri SDR source.
- [jketterl] Added Linux desktop icon for OpenWebRX.
- [jketterl] Fixed ThreadModule starting thread twice.
- [jketterl] Removed depdendency on SoapySDRUtils.

**1.2.46**
- Added list of active services to the Settings page.
- Added new toolbar icons, based on Google design.
- Added Help icon leading to documentation.
- Fixed race condition when sending map to a new client.
- Removed HL2 frequency workaround (fixed in hpsdrconnector).

**1.2.45**
- Added ability to delete files, when authorized.
- Added locking to connector-based SDR sources.
- Improved EIBI schedules display on the map.
- Fixed exception when disabling SDR source twice.
- Fixed HL2 noise after HL2 first initialized.
- No longer reporting AIS messages to IGATE.

**1.2.44**
- Added Storage API for creating files that avoids name collisions.
- Added admin-configurable FAX LPM parameter (default is 120).
- Added reference to documentation to the console window.
- Added maidenhead layer to Leaflet-based maps.
- Added waterfall color theme by Zoran (9A6NDZ).
- Fixed volume resetting to zero on page reload.
- Fixed step tuning when waterfall is zoomed.
- Fixed browser console error on vendor-provided markers.
- Increased upper limit on aircraft data retention to 100000 seconds.

**1.2.43**
- Added support for JS plugins developed by Stanislav Lechev.
- Added option to switch between US and EU RDS decoding.
- Added option to show dits and dahs when decoding CW.
- Refactored and improved CW, SITOR-B, and CCIR476 decoders.
- Reorganized "Demodulation and Decoding" settings page.
- Fixed info bubble not updating in Google map.
- Fixed resizing RDS display on mobile devices.
- Fixed date/time parsing in RDS display.
- Fixed CW decoder to print underscores for unrecognized characters.

**1.2.42**
- Added broadcast FM RDS decoder, using Redsea.
- Added bind_address core configuration parameter.
- Descreased SDR initialization retry time to 15 seconds.
- Stopped some failed sources from restarting indefinitely.
- Enabled nano-scroller in relevant panels on startup.

**1.2.41**
- Added message broadcasting function for admin.
- Added ability to disable chat between clients.
- Fixed Settings crash when a client has no SDR selected.
- Fixed colors resetting when tuning outside profile.
- Leaflet map now saves map and layer selections.

**1.2.40**
- Added chat between currently connected users.
- Added ability to manage clients connected via reverse proxy.
- The proxy has to provide correct X-Forwarded-For header.
- Relaxed policy so that only socket connections are banned.
- Moved all client-related code to client.py.
- Moved ColorCache implementation to color.py.

**1.2.39**
- Added connected clients display to the Settings page.
- Added ability to ban clients for chosen amount of time.
- Added ability to unban previously banned clients.
- Fixed agent string to make RepeaterBook work.
- Disabled buffering when saving logs from background decoders.

**1.2.38**
- Fixed primary modulation change with digital decoders.
- Fixed secondary frequency when changing bandpass.
- Fixed digital voice panel colors.
- Fixed volume and mute controls.
- Fixed NR controls.
- Added explanation of the RSPdx HDR mode.
- Updated HPSDR settings to Jakob's latest version.
- Allowed LSB as underlying CW decoder mode.

**1.2.37**
- Added "Settings" UI section for configuring user interface.
- Saving receiver and map UI settings in the browser storage.
- Removed themes, opacity, frame, wheel options from server settings.
- Animated UI sections collapse and expansion.
- Added RTTY, NAVTEX, and MSI bookmarks at proper offsets.
- Added "Black" UI theme.

**1.2.36**
- Added several UI themes, switched via "User interface color scheme".
- Made text console window contain more text (RTTY, CW, etc).
- Added nano-scroller to the text console window.
- Switched back to LRGB for mixing locator colors.
- Renamed "Range" section to "Display".

**1.2.35**
- Added SITOR-B / NAVTEX decoder.
- Fixed AIS map information bubbles.
- Used underscores for unrecognized CW/RTTY characters.

**1.2.34**
- Reworked locator info, adding colored band/mode designators.
- Improved locator square colors to also reflect reports' age.
- Linked HAM callsigns and AIS vessel IDs to respective websites.
- Added country name tooltips to HAM callsigns and AIS vessel IDs.
- Hopefully fixed FAX decoder randomly restarting on a new page.
- Moved common JavaScript functions to Utils.js.
- Fixed links on HFDL flight reports.
- Silenced EIBI log warnings.

**1.2.33**
- Syncing library versions with original OWRX 1.2.2.
- Refactored locators map display.
- Assigned each locator a single rectangle.
- Rectangle's transparency reflects number and age of reports.
- Rectangle's hue represents reported bands.
- Removed overlapping edges from rectangles.
- Added time-to-live to EIBI markers.
- Added LSimpleMarker.
- Fixed, updated, optimized EIBI database algorithms and data.
- Fixed aircraft time-to-live values.

**1.2.32**
- Added separate display for ADSB flight data.
- Added separate class of aircraft markers.
- Added aircraft icons, by type and category.
- Added optional time-to-live to map markers.
- Added ability to run Tar1090 map together with OWRX+.
- Added squawk and signal strength to ADSB info bubbles.
- Now showing aircraft speed in knots, altitude in feet.
- Now using Dump1090 JSON data directly (via /tmp/dump1090).
- Optimized and simplified features display on the map.
- Fixed aircraft title linkify(), VDL2 altitudes, etc.
- Fixed Leaflet information bubbles.

**1.2.31**
- Added display of latest aircraft messages to the map.
- Adding parsing of the dump1090 JSON output (in progress).
- No longer preferring shorter EIBI entries to longer ones.
- Now loading fresh EIBI schedule every 24 hours.
- Fixed background ACARS service.
- Fixed missing SAM modulation.
- Fixed map info bubble formatting.
- Optimized locking in RepeaterBook and EIBI modules.

**1.2.30**
- Updated OpenWebRX+ with changes from Jakob's develop branch.
- Added Jakob's RTTY decoder and made it the default.
- Added ACARS aircraft protocol decoder, using AcarsDec.
- Added aircraft manager fusing data from multiple sources.
- Added background mode for HFDL, VDL2, ADSB, ACARS decoders.
- Added background aircraft map position updates.
- Added origin and destionation airport display (ACARS).
- Added links from aircraft messages to the map.
- Added default bookmarks for ACARS frequencies.
- Added SDRPlay High Dynamic Resolution (HDR) option.
- Device log now shown at the device settings page.
- Fixed a crash after switching from ADSB to other profiles.
- Fixed linkify() failing on aircraft IDs containing dash.
- Fixed repeater bookmarks to report NFM modulation.
- Fixed some APRS symbols to face east.
- Converting flight IDs from IATA (AAnnnn) to ICAO (AAAnnnn).
- Switched many digital IQ decoders to use EMPTY modulation.
- Switched TextParser to LineBasedModule base.
- Switched ISM decoder to use ExecModule.
- Optimized MultiMon-based digital decoders.
- Removed secondary ADSB waterfall to improve performance.
- Painted YES/NO feature indicators red and green.
- Changed MODE-S ID lookup URL to FlightAware.

**1.2.29**
- Added worldwide OpenWeatherMap support (needs key).
- Added NFM to SSTV underlying modes (needs testing).
- Added configurable FAX options (post-processing, etc).
- Added configurable aircraft data expiration times.
- Improved aircraft data maintenance and merging.
- Improved SWL bookmarks generation (via EIBI).
- Improved FAX decoding, can receive photos now.
- Changed FAX bookmarks to be 1.9kHz below carrier.
- Dropped FAX input frequency to 12kHz.
- Optimized SSTV, FAX, RTTY, and CW decoders.
- Fixed ISM parser with correct ColorCache object.
- ADSB airplanes are red now, VDL2/HFDL are blue.

**1.2.28**
- Updated CSDR and PyCSDR with latest changes from Jakob's develop branch.
- DumpHFDL, DumpVDL2, and Dump1090 now available from Jakob's repository.
- Added ADSB aircraft protocol decoder, using Dump1090 and ExecModule.
- Added AircraftManager storing data from all aircraft decoders.
- Added DumpHFDL, DumpVDL2, Dump1090 to recommended packages.
- Added Mode-S (ADSB) message parser by Jakob Ketterl.
- Added OpenSeaMap and WeatherRadar Leaflet layers by Stanislav Lechev.
- Added shadows to aircraft on the map, based on altitudes.
- Improved aircraft message display, common for all three decoders.
- Fixed OpenWebRX service hanging up when stopped.
- Fixed orientation of north-facing APRS symbols.
- Fixed VDL2 logs not showing up in file browser.
- Changed rf_gain in the default SDRPlay profile to "auto".
- RepeaterBook now queried for up to 200km.

**1.2.27**
- Added VDL2 aircraft protocol decoder, using DumpVDL2.
- Added standard VDL2 frequencies to the default bookmarks.
- VDL2 data is shown both as text and as map markers.
- Added repeater search via RepeaterBook.com.
- Added range setting (km) for showing repeaters in.
- Repeaters are shown both on the map and as bookmarks.
- Fixed non-APRS (YSF, etc) markers not showing up.
- Further improved parsing EIBI schedules.
- Simplified a lot of JavaScript code.

**1.2.26**
- Added autogenerated bookmarks based on EIBI schedules.
- Set bookmark search range (km) in "Settings | General | Display".
- The bookmark search range can also be set per profile.
- Set range to 0km to disable autogenerated bookmarks (default).
- Fixed locked source switch resetting it for all connections.
- Separated default bookmarks by type, removing rarely used.
- Fixed profile setting cues blowing up page layout.
- Fixed fax frequency for Pevek.
- Improved EIBI parser a bit.

**1.2.25**
- Refactored maps, extracting implementation independent code.
- Added Leaflet-based maps by Stanislav Lechev (LZ2SLL).
- OpenStreetMap and other free maps are available via Leaflet.
- Default to Google or Leaflet maps via the Settings.
- Clicking toolbar map button toggles between Google and Leaflet.
- Clicking UTC clock display toggles map controls.
- Added several more target areas to the EIBI parser.
- Now assuming any EIBI entry below 4.8MHz to be USB (was 7MHz).

**1.2.24**
- Added support for EIBI shortwave schedules.
- Schedules updated monthly from the EIBI website.
- Map shows currently active transmitters, with 1-hour schedules.
- You can instantly tune by clicking on a schedule entry.
- Your current SDR profile must contain the clicked frequency.

**1.2.23**
- Added OpenWebRX, WebSDR, and KiwiSDR locations to the map.
- Added periodic updates of online SDR locations from the web.
- Added ability to toggle map markers, by type.
- Started adding support for EIBI shortwave schedules.

**1.2.22**
- Added proper support for multiple bookmark files.
- Place extra bookmark files into /etc/openwebrx/bookmarks.d.
- Only /var/lib/openwebrx/bookmarks.json file is UI-editable.
- Synchronized UTC clock changes with the minute changes.
- Made SDR sources retry startup up to ten times, if it fails.
- Made status bar, log, and console scale on mobile devices.
- Made OWRX discover /sys node containing CPU temperature.
- Multiple improvements to the Docker build, made by LZ2SLL.
- Added LPD433 band, KDR444, RHA68, MURS bookmarks.

**1.2.21**
- Added CPU temperature to the CPU load display.
- Added UTC clock to the receiver panel.
- Added default bookmarks.json file with some common bookmarks.
- Fixed secondary waterfall requiring FFT compression.
- Fixed center_freq changes not propagating up.
- Extended 2m and 70cm bands to reflect US definitions.
- Made ISM device model column wider.

**1.2.20**
- Increased ISM mode bandwidth from 48kHz to 250kHz.
- Added admin-defined receiver name (if any) to the window title.
- Made scanner continue scan from the last active bookmark.
- Fixed CSDR crashing OWRX at >48kHz NFM deemphasis bandwidths.
- Fixed Soapy extra settings being sent as individual values.
- Fixed Settings icon getting cut off in Chrome on Android.
- Fixed number input dialog shifting the UI on mobile devices.
- Fixed accidental resize on mobile devices.
- Optimized CW decoder, RTTY, SSTV, FAX operation in CSDR.
- Now killing slave process if it does not quit in 3 seconds.
- Added 8m amateur band.

**1.2.19**
- Added separate ZVEI decoder for German SELCALL modes.
- Added device option to require magic key for profile changes.
- Added option to swap mouse wheel between tuning and zooming.
- Added optional frame to bookmark dialogs.
- Updated column names and formatting for PAGE, HFDL, ISM panels.
- Updated rtl-433 invocation to be compatible with older versions.
- Renamed HFDL background service output to "HFDL-*".
- Changed "pocsag" mode to "page" in bands.json.

**1.2.18**
- Integrated rtl-433 and dumphfdl decoder tools.
- Added universal PAGE decoder (POCSAG + FLEX) via multimon-ng.
- Added ISM decoder via rtl-433.
- Added HFDL decoder via dumphfdl.
- Added color identification for pager addresses.
- Added optional filter to only show readable pager messages.
- Added file browser support for text logs (such as ISM or HFDL).
- Added HFDL-based aircraft display to the map.
- Enabled background service functionality for HFDL, ISM, and PAGE.
- Enabled squelch support for SELCALL, SSTV, and FAX decoders.
- Changed read() to read1() in PopenModule to get immediate input.
- Made PopenModule kill process that refuses to terminate on its own.
- Disabled the original POCSAG decoder, superseded by the new one.
- Added 433.92MHz ISM frequency to the bandplan.
- Added 6.25kHz and 8.33kHz tuning steps.

**1.2.17**
- Integrated multimon-ng digital mode decoding suite.
- Added FLEX paging protocol decoder, provided by multimon-ng.
- Added SELCALL decoders for EEA, EIA, CCIR, DTMF standards.
- Fixed center frequency modifications surviving profile change.
- Fixed waterfall colors resetting when changing center frequency.
- Fixed background decoding cases using resampler.

**1.2.16**
- Added ability to change center frequency by right-clicking arrow buttons.
- Added an option to allow audio recording (on by default).
- Added an option to allow center frequency changes (off by default).
- Added an option to require magic key for center frequency changes.
- Added 10Hz, 20Hz, and 50Hz steps for CW listeners.

**1.2.15**
- Added scanner, enabled with right click on SQ button.
- Scanner scans bookmarks using the current squelch level.

**1.2.14**
- Added automatic image conversion to PNG (requires ImageMagick).
- Ported MSK144 decoder from Jakob's development OWRX branch.
- Improved FAX parser, fixing several issues.
- Fixed color order issue with SSTV and FAX displays.
- Fixed several issues in the SSTV parser.
- Moved 4m band edges to fit most country-specific allocations.

**1.2.13**
- Added synchronous AM demodulator (SAM).
- Added 12.5kHz and 25kHz tuning steps.
- Extended default FAX page length to 1400 lines.
- Fixed bandpass bounds resetting after any frequency change.
- Fixed bandpass indicator labels cutting off.
- Fixed file browser, restricting all shots to 32% width.
- Fixed several bugs in the background FAX decoder.
- Made OWRX package depend on the latest PyCSDR package.

**1.2.12**
- Added FAX decoder, tested on weather fax transmissions.
- Added FAX background decoding service.
- Added option to ignore indirect APRS reports.
- Fixed a minor JavaScript error on startup.
- Optimized SSTV decoder code.

**1.2.11**
- Made receiver panel collapsible, to free screen estate.
- Now tracking and displaying paths taken by APRS packets.
- Added option to draw a frame around the receiver panel.
- Added option to prefer direct APRS reports to relayed ones.
- Added map option to turn off the colored squares.
- Added 145.825MHz APRS frequency for the ISS repeater.
- Fixed waterfall hangup when zooming at the edge of a band.
- Fixed computing paths traversed by APRS packets.

**1.2.10**
- Added spectrum display, toggled with a receiver panel button.
- Added a setting to change how opaque the user interface is.

**1.2.9**
- Fixed missing 'N' letters in RTTY and CW decoders output.
- Fixed SSTV decoder getting stuck after receiving 2-3 images.
- Added SSTV debug messages to the log.
- Removed some unused SSTV frequencies from band plan.
- Removed SSTV NFM mode, since either USB or can be used with NFM.
- Multiple other small fixes and style changes.

**1.2.8**
- Added AIS vessel reporting, with the map and background service.
- Added configurable URL for looking up vessels by their MMSIs.
- Added Air and Marine service bands to the band plan.
- Added more SSTV frequencies to the band plan.
- Declared LSB and FM as modes supported by SSTV.
- Refactored file storage mechanism.

**1.2.7**
- Added MP3 recorder for saving received audio to files.
- Added "Files" page for viewing received SSTV frames.
- Added automatic deletion of previously received files.
- Added setting for how many received files should be kept.
- Clicking on an SSTV frame now saves it to a file.

**1.2.6**
- Added SSTV decoder with user interface.
- Added background SSTV decoding to /tmp folder.
- Extended CB band up to 28MHz, as used in some countries.
- Added SSTV and RTTY frequencies to the bands layout.

**1.2.5**
- Added RTTY decoder.
- Improved CW decoder.
- Fixed possible crash in CW chain.
- Switched both decoders to complex input.
- Can now use SHIFT with scroll wheel, as mouse button.

**1.2.4**
- Added automated CW decoder (experimental).
- Added scroll wheel support to frequency scale.
- Added changing bandpass bounds with scroll wheel.
- Added optional HTTPS support.
- Fixed frequency jumping to last input value.
- Made tuning buttons bigger.

**1.2.3**
- Added configurable session timeout option, with a default page.
- Made multiple user interface improvements for touch screens.
- Made touch-and-drag panning more reliable.
- Added zoom in/out with the stretch/pinch gesture.
- Added buttons for precisely touch-tuning the frequency.

**1.2.2**
- Added noise filter based on spectral subtraction.
- Added configurable tuning step.
- Added support for panning on touch screens.
- Made OWRX tune to the CW frequency in the CW mode.
- Improved APRS information display.

**1.2.1**
- FifiSDR support fixed (pipeline formats now line up correctly)
- Added "Device" input for FifiSDR devices for sound card selection

**1.2.0**
- Major rewrite of all demodulation components to make use of the new csdr/pycsdr and digiham/pydigiham demodulator
  modules
- Preliminary display of M17 callsign information
- New devices supported:
  - Blade RF

**1.1.0**
- Reworked most graphical elements as SVGs for faster loadtimes and crispier display on hi-dpi displays
- Updated pipelines to match changes in digiham
- Changed D-Star and NXDN integrations to use new decoders from digiham
- Added D-Star and NXDN metadata display

**1.0.0**
- Introduced `squelch_auto_margin` config option that allows configuring the auto squelch level
- Removed `port` configuration option; `rtltcp_compat` takes the port number with the new connectors
- Added support for new WSJT-X modes FST4, FST4W (only available with WSJT-X 2.3) and Q65 (only avilable with
  WSJT-X 2.4)
- Added support for demodulating M17 digital voice signals using m17-cxx-demod
- New reporting infrastructure, allowing WSPR and FST4W spots to be sent to wsprnet.org
- Add some basic filtering capabilities to the map
- New arguments to the `openwebrx` command-line to facilitate the administration of users (try `openwebrx admin`)
- Default bandwidth changes:
  - "WFM" changed to 150kHz
  - "Packet" (APRS) changed to 12.5kHz
- Configuration rework:
  - New: fully web-based configuration interface
  - System configuration parameters have been moved to a new, separate `openwebrx.conf` file
  - Remaining parameters are now editable in the web configuration
  - Existing `config_webrx.py` files will still be read, but changes made in the web configuration will be written to
    a new storage system
  - Added upload of avatar and panorama image via web configuration
- New devices supported:
  - HPSDR devices (Hermes Lite 2) thanks to @jancona
  - BBRF103 / RX666 / RX888 devices supported by libsddc
  - R&S devices using the EB200 or Ammos protocols

**0.20.3**
- Fix a compatibility issue with python versions <= 3.6

**0.20.2**
- Fix a security problem that allowed arbitrary commands to be executed on the receiver
  ([See github issue #215](https://github.com/jketterl/openwebrx/issues/215))

**0.20.1**
- Remove broken OSM map fallback

**0.20.0**
- Added the ability to sign multiple keys in a single request, thus enabling multiple users to claim a single receiver
  on receiverbook.de
- Fixed file descriptor leaks to prevent "too many open files" errors
- Add new demodulator chain for FreeDV
- Added new HD audio streaming mode along with a new WFM demodulator
- Reworked AGC code for better results in AM, SSB and digital modes
- Added support for demodulation of "Digital Radio Mondiale" (DRM) broadcast using the "dream" decoder.
- New default waterfall color scheme
- Prototype of a continuous automatic waterfall calibration mode
- New devices supported:
  - FunCube Dongle Pro+ (`"type": "fcdpp"`)
  - Support for connections to rtl_tcp (`"type": "rtl_tcp"`)

**0.19.1**
- Added ability to authenticate receivers with listing sites using "receiver id" tokens

**0.19.0**
- Fix direwolf connection setup by implementing a retry loop
- Pass direct sampling mode changes for rtl_sdr_soapy to owrx_connector
- OSM maps instead of Google when google_maps_api_key is not set (thanks @jquagga)
- Improved logic to pass parameters to soapy devices.
  - `rtl_sdr_soapy`: added support for `bias_tee`
  - `sdrplay`: added support for `bias_tee`, `rf_notch` and `dab_notch`
  - `airspy`: added support for `bitpack`
- Added support for Perseus-SDR devices, (thanks @amontefusco)
- Property System has been rewritten so that defaults on sdr behave as expected
- Waterfall range auto-adjustment now only takes the center 80% of the spectrum into account, which should work better
  with SDRs that oversample or have rather flat filter curves towards the spectrum edges
- Bugfix for negative network usage
- FiFi SDR: prevent arecord from shutting down after 2GB of data has been sent
- Added support for bias tee control on rtl_sdr devices
- All connector driven SDRs now support `"rf_gain": "auto"` to enable AGC
- `rtl_sdr` type now also supports the `direct_sampling` option
- Added decoding implementation for for digimode "JS8Call"
  (requires an installation of [js8call](http://js8call.com/) and
  [the js8py library](https://github.com/jketterl/js8py))
- Reorganization of the frontend demodulator code
- Improve receiver load time by concatenating javascript assets
- Docker images migrated to Debian slim images; This was necessary to allow the use of function multiversioning in
  csdr and owrx_connector to allow the images to run on a wider range of CPUs
- Docker containers have been updated to include the SDRplay driver version 3
- HackRF support is now based on SoapyHackRF
- Removed sdr.hu server listing support since the site has been shut down
- Added support for Radioberry 2 Rasbperry Pi SDR Cape

**0.18.0**
- Support for SoapyRemote

**2020-02-08**
- Compression, resampling and filtering in the frontend have been rewritten in javascript, sdr.js has been removed
- Decoding of Pocsag modulation is now possible
- Removed the 3D waterfall since it had no real application and required ~1MB of javascript code to be downloaded
- Improved the frontend handling of the "too many users" scenario
- PSK63 digimode is now available (same decoding pipeline as PSK31, but with adopted parameters)
- The frequency can now be manipulated with the mousewheel, which should allow the user to tune more precise. The tuning
  step size is determined by the digit the mouse cursor is hovering over.
- Clicking on the frequency now opens an input for direct frequency selection
- URL hashes have been fixed and improved: They are now updated automatically, so a shared URL will include frequency
  and demodulator, which allows for improved sharing and linking.
- New daylight scheduler for background decoding, allows profiles to be selected by local sunrise / sunset times
- New devices supported:
  - LimeSDR (`"type": "lime_sdr"`)
  - PlutoSDR (`"type": "pluto_sdr"`)
  - RTL_SDR via Soapy (`"type": "rtl_sdr_soapy"`) on special request to allow use of the direct sampling mode

**2020-01-04**
- The [owrx_connector](https://github.com/jketterl/owrx_connector) is now the default way of communicating with sdr
  devices. The old sdr types have been replaced, all `_connector` suffixes on the type must be removed!
- The sources have been refactored, making it a lot easier to add support for other devices
- SDR device failure handling has been improved, including user feedback
- New devices supported:
  - FiFiSDR (`"type": "fifi_sdr"`)

**2019-12-15**
- wsjt-x updated to 2.1.2
- The rtl_tcp compatibility mode of the owrx_connector is now configurable using the `rtltcp_compat` flag

**2019-12-10**
- added support for airspyhf devices (Airspy HF+ / Discovery)

**2019-12-05**
- explicit device filter for soapy devices for multi-device setups

**2019-12-03**
- compatibility fixes for safari browsers (ios and mac)

**2019-11-24**
- There is now a new way to interface with SDR hardware, .
  They talk directly to the hardware (no rtl_sdr / rx_sdr necessary) and offer I/Q data on a socket, just like nmux
  did before. They additionally offer a control socket that allows openwebrx to control the SDR parameters directly,
  without the need for repeated restarts. This allows for quicker profile changes, and also reduces the risk of your
  SDR hardware from failing during the switchover. See `config_webrx.py` for further information and instructions.
- Offset tuning using the `lfo_offset` has been reworked in a way that `center_freq` has to be set to the frequency you
  actually want to listen to. If you're using an `lfo_offset` already, you will probably need to change its sign.
- `initial_squelch_level` can now be set on each profile.
- As usual, plenty of fixes and improvements.

**2019-10-27**
- Part of the frontend code has been reworked
  - Audio buffer minimums have been completely stripped. As a result, you should get better latency. Unfortunately,
    this also means there will be some skipping when audio starts.
  - Now also supports AudioWorklets (for those browser that have it). The Raspberry Pi image has been updated to include
    https due to the SecureContext requirement.
  - Mousewheel controls for the receiver sliders
- Error handling for failed SDR devices

**2019-09-29**
- One of the most-requested features is finally coming to OpenWebRX: Bookmarks (sometimes also referred to as labels).
  There's two kinds of bookmarks available:
  - Serverside bookmarks that are set up by the receiver administrator. Check the file `bookmarks.json` for examples!
  - Clientside bookmarks which every user can store for themselves. They are stored in the browser's localStorage.
- Some more bugs in the websocket handling have been fixed.

**2019-09-25**
- Automatic reporting of spots to [pskreporter](https://pskreporter.info/) is now possible. Please have a look at the
  configuration on how to set it up.
- Websocket communication has been overhauled in large parts. It should now be more reliable, and failing connections
  should now have no impact on other users.
- Profile scheduling allows to set up band-hopping if you are running background services.
- APRS now has the ability to show symbols on the map, if a corresponding symbol set has been installed. Check the
  config!
- Debug logging has been disabled in a handful of modules, expect vastly reduced output on the shell.

**2019-09-13**
- New set of APRS-related features
  - Decode Packet transmissions using [direwolf](https://github.com/wb2osz/direwolf) (1k2 only for now)
  - APRS packets are mostly decoded and shown both in a new panel and on the map
  - APRS is also available as a background service
  - direwolfs I-gate functionality can be enabled, which allows your receiver to work as a receive-only I-gate for the
    APRS network in the background
- Demodulation for background services has been optimized to use less total bandwidth, saving CPU
- More metrics have been added; they can be used together with collectd and its curl_json plugin for now, with some
  limitations.

**2019-07-21**
- Latest Features:
  - More WSJT-X modes have been added, including the new FT4 mode
  - I started adding a bandplan feature, the first thing visible is the "dial" indicator that brings you right to the
    dial frequency for digital modes
  - fixed some bugs in the websocket communication which broke the map

**2019-07-13**
- Latest Features:
  - FT8 Integration (using wsjt-x demodulators)
  - New Map Feature that shows both decoded grid squares from FT8 and Locations decoded from YSF digital voice
  - New Feature report that will show what functionality is available
- There's a new Raspbian SD Card image available (see below)

**2019-06-30**
- I have done some major rework on the openwebrx core, and I am planning to continue adding more features in the near
  future. Please check this place for updates.
- My work has not been accepted into the upstream repository, so you will need to chose between my fork and the official
  version.
- I have enabled the issue tracker on this project, so feel free to file bugs or suggest enhancements there!
- This version sports the following new and amazing features:
  - Support of multiple SDR devices simultaneously
  - Support for multiple profiles per SDR that allow the user to listen to different frequencies
  - Support for digital voice decoding
  - Feature detection that will disable functionality when dependencies are not available (if you're missing the digital
    buttons, this is probably why)
- Raspbian SD Card Images and Docker builds available (see below)
- I am currently working on the feature set for a stable release, but you are more than welcome to test development
  versions!
