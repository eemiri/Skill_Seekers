# PowerShell helpers to switch Claude Code between Anthropic, Z.AI, and DeepSeek.
# It pulls Z.AI/DeepSeek tokens and defaults from .zprofile if they are not already set.

$repoRoot = $PSScriptRoot
$zProfilePath = Join-Path $repoRoot ".zprofile"

function Import-ZProfileTokens {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        return
    }

    $content = Get-Content -Raw -Path $Path

    if (-not $Env:Z_AI_AUTH_TOKEN) {
        $m = [regex]::Match($content, 'Z_AI_AUTH_TOKEN="([^"]+)"')
        if ($m.Success) { $Env:Z_AI_AUTH_TOKEN = $m.Groups[1].Value }
    }
    if (-not $Env:Z_AI_BASE_URL) {
        $m = [regex]::Match($content, 'Z_AI_BASE_URL="([^"]+)"')
        if ($m.Success) { $Env:Z_AI_BASE_URL = $m.Groups[1].Value }
    }

    if (-not $Env:DEEPSEEK_AUTH_TOKEN) {
        $m = [regex]::Match($content, 'DEEPSEEK_AUTH_TOKEN="([^"]+)"')
        if ($m.Success) { $Env:DEEPSEEK_AUTH_TOKEN = $m.Groups[1].Value }
    }
    if (-not $Env:DEEPSEEK_BASE_URL) {
        $m = [regex]::Match($content, 'DEEPSEEK_BASE_URL="([^"]+)"')
        if ($m.Success) { $Env:DEEPSEEK_BASE_URL = $m.Groups[1].Value }
    }
    if (-not $Env:DEEPSEEK_API_TIMEOUT_MS) {
        $m = [regex]::Match($content, 'DEEPSEEK_API_TIMEOUT_MS=([0-9]+)')
        if ($m.Success) { $Env:DEEPSEEK_API_TIMEOUT_MS = $m.Groups[1].Value }
    }
    if (-not $Env:DEEPSEEK_MODEL) {
        $m = [regex]::Match($content, 'DEEPSEEK_MODEL=([^\s]+)')
        if ($m.Success) { $Env:DEEPSEEK_MODEL = $m.Groups[1].Value }
    }
    if (-not $Env:DEEPSEEK_SMALL_FAST_MODEL) {
        $m = [regex]::Match($content, 'DEEPSEEK_SMALL_FAST_MODEL=([^\s]+)')
        if ($m.Success) { $Env:DEEPSEEK_SMALL_FAST_MODEL = $m.Groups[1].Value }
    }
    if (-not $Env:DEEPSEEK_CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC) {
        $m = [regex]::Match($content, 'DEEPSEEK_CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=([^\s]+)')
        if ($m.Success) { $Env:DEEPSEEK_CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = $m.Groups[1].Value }
    }
}

Import-ZProfileTokens -Path $zProfilePath

function ca {
    Remove-Item Env:ANTHROPIC_API_KEY -ErrorAction SilentlyContinue
    Remove-Item Env:ANTHROPIC_AUTH_TOKEN -ErrorAction SilentlyContinue
    $Env:ANTHROPIC_BASE_URL = "https://api.anthropic.com"
    claude @args
}

function zc {
    Remove-Item Env:ANTHROPIC_AUTH_TOKEN -ErrorAction SilentlyContinue
    $Env:ANTHROPIC_BASE_URL = if ($Env:Z_AI_BASE_URL) { $Env:Z_AI_BASE_URL } else { "https://api.z.ai/api/anthropic" }
    $Env:ANTHROPIC_API_KEY = $Env:Z_AI_AUTH_TOKEN
    claude @args
}

function dc {
    Remove-Item Env:ANTHROPIC_AUTH_TOKEN -ErrorAction SilentlyContinue
    $Env:ANTHROPIC_BASE_URL = if ($Env:DEEPSEEK_BASE_URL) { $Env:DEEPSEEK_BASE_URL } else { "https://api.deepseek.com/anthropic" }
    $Env:ANTHROPIC_API_KEY = $Env:DEEPSEEK_AUTH_TOKEN
    if ($Env:DEEPSEEK_API_TIMEOUT_MS) { $Env:ANTHROPIC_TIMEOUT_MS = $Env:DEEPSEEK_API_TIMEOUT_MS }
    if ($Env:DEEPSEEK_MODEL) { $Env:ANTHROPIC_MODEL = $Env:DEEPSEEK_MODEL }
    if ($Env:DEEPSEEK_SMALL_FAST_MODEL) { $Env:ANTHROPIC_SMALL_FAST_MODEL = $Env:DEEPSEEK_SMALL_FAST_MODEL }
    if ($Env:DEEPSEEK_CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC) { $Env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = $Env:DEEPSEEK_CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC }
    claude @args
}
