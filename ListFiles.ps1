$directoryPath = "C:\Code\flaskProject9\" # Replace with your directory path

Get-ChildItem -Path $directoryPath -File | ForEach-Object {
    Write-Output "## $($_.Name) ##"
    Get-Content $_.FullName
    Write-Output "`n" # Adds a newline for separation between files
}
