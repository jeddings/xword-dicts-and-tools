<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" indent="yes" omit-xml-declaration="yes" media-type="text/plain"/>
<xsl:template match="/">
<xsl:text disable-output-escaping="yes">&lt;ACROSS PUZZLE V2&gt;</xsl:text><xsl:text>&#xa;</xsl:text>
<xsl:text disable-output-escaping="yes">&lt;TITLE&gt;</xsl:text><xsl:text>&#xa;</xsl:text>
    <xsl:value-of select="/CROSSFIRE/TITLE"/><xsl:text>&#xa;</xsl:text>
<xsl:text disable-output-escaping="yes">&lt;AUTHOR&gt;</xsl:text>
    Jeff Eddings<xsl:text>&#xa;</xsl:text>
<xsl:text disable-output-escaping="yes">&lt;COPYRIGHT&gt;</xsl:text><xsl:text>&#xa;</xsl:text>
    <xsl:value-of select="/CROSSFIRE/COPYRIGHT"/><xsl:text>&#xa;</xsl:text>
<xsl:text disable-output-escaping="yes">&lt;SIZE&gt;</xsl:text>
    15x15<xsl:text>&#xa;</xsl:text>
<xsl:text disable-output-escaping="yes">&lt;GRID&gt;</xsl:text>
    <xsl:value-of select="/CROSSFIRE/GRID"/>
<xsl:text disable-output-escaping="yes">&lt;ACROSS&gt;</xsl:text><xsl:text>&#xa;</xsl:text>
    <xsl:for-each select="/CROSSFIRE/WORDS/WORD">
      <xsl:if test="@dir='ACROSS'">
    <xsl:value-of select="."/><xsl:text>&#xa;</xsl:text> 
      </xsl:if>
    </xsl:for-each>
<xsl:text disable-output-escaping="yes">&lt;DOWN&gt;</xsl:text><xsl:text>&#xa;</xsl:text>
    <xsl:for-each select="/CROSSFIRE/WORDS/WORD">
      <xsl:if test="@dir='DOWN'"><xsl:value-of select="."/><xsl:text>&#xa;</xsl:text></xsl:if></xsl:for-each></xsl:template></xsl:stylesheet>
