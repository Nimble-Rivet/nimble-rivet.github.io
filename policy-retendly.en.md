# Retendly Privacy Policy

Publisher: **Nimble Rivet**. App and privacy contact: **nimblerivet@gmail.com**.
Last updated: **October 29, 2026**.

## Data and purposes

Retendly helps you plan recurring tasks and keep a completion history. It processes the reminder titles and descriptions, repeat intervals, due dates, completion dates, notes and archive status you enter. This information supports reminders, next-due calculations, history, the home-screen widget and notifications. Notification settings and technical delivery records are also stored on your device.

Core features use a local database and do not require a Nimble Rivet account. The current app contains no advertising, built-in analytics or crash reporting to the developer's servers. Reminder contents are not automatically sent to a Nimble Rivet server.

## Notifications and Android access

Notification permission is used for reminders and the overdue digest. Exact-alarm access allows notifications to be scheduled for the selected time. The app restores its schedule after the device restarts. Reminder text may appear in notifications and the widget; lock-screen visibility depends on your Android settings.

## File export and import

When you request it, the app creates an INI file containing reminders, archived reminders and history, including notes. You select its destination using Android's system file picker. If you choose a cloud document provider, that provider receives and handles the file under its own rules. During import, Retendly reads and validates your selected file and displays a preview; applying the data requires your confirmation.

INI files are plain text and are not encrypted by the app. Anyone who receives a file can read it. Exported copies are stored separately from the app and must be deleted in the destination you selected.

## Optional Google Drive backups

In builds with a configured Google Drive integration, you may separately connect your Google account and authorize access to Retendly's private app-data space in Drive. The app requests access to this space rather than to all files in your Drive. Google Play services handles sign-in and permissions; your Google account password is not provided to Retendly.

To identify the connected account, Retendly uses its email address and technical Google Drive identifier. When a backup is created, reminder and history contents are sent directly to Google Drive over HTTPS. The file is accompanied by the device name, a random installation identifier, snapshot date, size and checksum so backups can be distinguished and checked. Authorization tokens are not included in backup files.

Automatic backups are initially off and can be enabled separately. After a successful backup, the app attempts to retain the seven most recent backups for the current installation. A cleanup failure may leave additional copies. Reinstalling creates a new installation, which does not automatically clean up the previous installation's copies. Disconnecting Google Drive in Retendly stops jobs on that device and removes local connection details, but does not delete cloud backups or disconnect other devices. Manage cloud data and app authorization through Google Drive and your Google account. Google handles data under its privacy policy: https://policies.google.com/privacy.

## Android system backup

The app permits Android system backup and device transfer. Depending on your device, account and provider settings, system services may copy the local database and preferences. This is separate from connecting Google Drive within Retendly. The app excludes notification delivery records, cloud connection details and pending cloud-transfer state from backup. Manage system backups in Android settings and with the relevant provider.

## Retention, deletion and protection

Local records remain until you change or delete them. Archiving preserves a reminder and its history. Permanently deleting a reminder removes it and its linked history; separately recovered history without a reminder may remain in the app. Clearing Retendly's data in Android settings or uninstalling the app removes its local data. Exported, cloud and system backups must be deleted separately and may otherwise be used for restoration.

Retendly uses Android's app-data isolation and HTTPS for Google Drive connections. It does not add its own encryption to the local database or INI backups. The security of your device, account and chosen storage affects access to your information.

## Contact and policy changes

When you email **nimblerivet@gmail.com**, your mail provider transmits your sender address, message and attachments. This information is used to respond to your request; send only the information needed for it. Use the same address for questions about data handling and deletion of information you have sent to support yourself.

This policy will be updated when data handling changes. It describes Retendly's features; the availability of optional features depends on your installed build and the configuration of external services.
