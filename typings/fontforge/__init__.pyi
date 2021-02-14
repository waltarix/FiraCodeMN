from __future__ import annotations

from typing import Any, Iterator

hooks: Any
spiroCorner: int
spiroG2: int
spiroG4: int
spiroLeft: int
spiroOpen: int
spiroRight: int
splineCorner: int
splineCurve: int
splineHVCurve: int
splineTangent: int
unspecifiedMathValue: int


def IsFraction(*args, **kwargs) -> Any: ...
def IsLigature(*args, **kwargs) -> Any: ...
def IsOtherFraction(*args, **kwargs) -> Any: ...
def IsVulgarFraction(*args, **kwargs) -> Any: ...
def SpiroVersion(*args, **kwargs) -> Any: ...
def UnicodeAnnotationFromLib(*args, **kwargs) -> Any: ...
def UnicodeBlockCountFromLib(*args, **kwargs) -> Any: ...
def UnicodeBlockEndFromLib(*args, **kwargs) -> Any: ...
def UnicodeBlockNameFromLib(*args, **kwargs) -> Any: ...
def UnicodeBlockStartFromLib(*args, **kwargs) -> Any: ...
def UnicodeNameFromLib(*args, **kwargs) -> Any: ...
def UnicodeNames2FrmTabFromLib(*args, **kwargs) -> Any: ...
def UnicodeNames2FromLib(*args, **kwargs) -> Any: ...
def UnicodeNames2GetCntFromLib(*args, **kwargs) -> Any: ...
def UnicodeNames2GetNxtFromLib(*args, **kwargs) -> Any: ...
def UnicodeNames2NxtUniFromLib(*args, **kwargs) -> Any: ...
def UnicodeNamesListVersion(*args, **kwargs) -> Any: ...
def activeFont(*args, **kwargs) -> Any: ...
def activeFontInUI(*args, **kwargs) -> Any: ...
def activeGlyph(*args, **kwargs) -> Any: ...
def activeLayer(*args, **kwargs) -> Any: ...
def ask(*args, **kwargs) -> Any: ...
def askChoices(*args, **kwargs) -> Any: ...
def askString(*args, **kwargs) -> Any: ...
def defaultOtherSubrs(*args, **kwargs) -> Any: ...
def fonts(*args, **kwargs) -> Any: ...
def fontsInFile(*args, **kwargs) -> Any: ...
def getPrefs(*args, **kwargs) -> Any: ...
def hasSpiro(*args, **kwargs) -> Any: ...
def hasUserInterface(*args, **kwargs) -> Any: ...
def loadEncodingFile(*args, **kwargs) -> Any: ...
def loadNamelist(*args, **kwargs) -> Any: ...
def loadNamelistDir(*args, **kwargs) -> Any: ...
def loadPrefs(*args, **kwargs) -> Any: ...
def logWarning(*args, **kwargs) -> Any: ...
def nameFromUnicode(*args, **kwargs) -> Any: ...
def onAppClosing(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Font: ...
def openFilename(*args, **kwargs) -> Any: ...
def parseTTInstrs(*args, **kwargs) -> Any: ...
def postError(*args, **kwargs) -> Any: ...
def postNotice(*args, **kwargs) -> Any: ...
def preloadCidmap(*args, **kwargs) -> Any: ...
def printSetup(*args, **kwargs) -> Any: ...
def readOtherSubrsFile(*args, **kwargs) -> Any: ...
def registerGlyphSeparationHook(*args, **kwargs) -> Any: ...
def registerImportExport(*args, **kwargs) -> Any: ...
def registerMenuItem(*args, **kwargs) -> Any: ...
def runInitScripts(*args, **kwargs) -> Any: ...
def saveFilename(*args, **kwargs) -> Any: ...
def savePrefs(*args, **kwargs) -> Any: ...
def scriptPath(*args, **kwargs) -> Any: ...
def setPrefs(*args, **kwargs) -> Any: ...
def ucFracChartGetCnt(*args, **kwargs) -> Any: ...
def ucLigChartGetAltCnt(*args, **kwargs) -> Any: ...
def ucLigChartGetAltVal(*args, **kwargs) -> Any: ...
def ucLigChartGetCnt(*args, **kwargs) -> Any: ...
def ucLigChartGetLoc(*args, **kwargs) -> Any: ...
def ucLigChartGetNxt(*args, **kwargs) -> Any: ...
def ucLigChartUGetAltCnt(*args, **kwargs) -> Any: ...
def ucLigChartUGetAltVal(*args, **kwargs) -> Any: ...
def ucOFracChartGetAltCnt(*args, **kwargs) -> Any: ...
def ucOFracChartGetAltVal(*args, **kwargs) -> Any: ...
def ucOFracChartGetCnt(*args, **kwargs) -> Any: ...
def ucOFracChartGetLoc(*args, **kwargs) -> Any: ...
def ucOFracChartGetNxt(*args, **kwargs) -> Any: ...
def ucOFracChartUGetAltCnt(*args, **kwargs) -> Any: ...
def ucOFracChartUGetAltVal(*args, **kwargs) -> Any: ...
def ucVulChartGetAltCnt(*args, **kwargs) -> Any: ...
def ucVulChartGetAltVal(*args, **kwargs) -> Any: ...
def ucVulChartGetCnt(*args, **kwargs) -> Any: ...
def ucVulChartGetLoc(*args, **kwargs) -> Any: ...
def ucVulChartGetNxt(*args, **kwargs) -> Any: ...
def ucVulChartUGetAltCnt(*args, **kwargs) -> Any: ...
def ucVulChartUGetAltVal(*args, **kwargs) -> Any: ...
def unParseTTInstrs(*args, **kwargs) -> Any: ...
def unicodeFromName(*args, **kwargs) -> Any: ...
def unitShape(*args, **kwargs) -> Any: ...
def version(*args, **kwargs) -> Any: ...


class awcontext:
    denom: Any = ...
    emSize: Any = ...
    font: Any = ...
    layer: Any = ...
    regionHeight: Any = ...


class awglyph:
    boundingbox: Any = ...
    glyph: Any = ...
    imaxY: Any = ...
    iminY: Any = ...
    left: Any = ...
    right: Any = ...


class contour:
    closed: Any = ...
    is_quadratic: Any = ...
    name: Any = ...
    spiro: Any = ...
    spiros: Any = ...
    __hash__: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addExtrema(self, *args, **kwargs) -> Any: ...
    def boundingBox(self, *args, **kwargs) -> Any: ...
    def cluster(self, *args, **kwargs) -> Any: ...
    def cubicTo(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def dup(self, *args, **kwargs) -> Any: ...
    def getSplineAfterPoint(self, *args, **kwargs) -> Any: ...
    def insertPoint(self, *args, **kwargs) -> Any: ...
    def isClockwise(self, *args, **kwargs) -> Any: ...
    def isEmpty(self, *args, **kwargs) -> Any: ...
    def lineTo(self, *args, **kwargs) -> Any: ...
    def makeFirst(self, *args, **kwargs) -> Any: ...
    def merge(self, *args, **kwargs) -> Any: ...
    def moveTo(self, *args, **kwargs) -> Any: ...
    def quadraticTo(self, *args, **kwargs) -> Any: ...
    def reverseDirection(self, *args, **kwargs) -> Any: ...
    def round(self, *args, **kwargs) -> Any: ...
    def selfIntersects(self, *args, **kwargs) -> Any: ...
    def similar(self, *args, **kwargs) -> Any: ...
    def simplify(self, *args, **kwargs) -> Any: ...
    def transform(self, *args, **kwargs) -> Any: ...
    def xBoundsAtY(self, *args, **kwargs) -> Any: ...
    def yBoundsAtX(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __iadd__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class cvt:
    font: Any = ...
    def find(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iadd__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class font:
    activeLayer: Any = ...
    ascent: Any = ...
    bitmapSizes: Any = ...
    capHeight: Any = ...
    changed: Any = ...
    cidcopyright: Any = ...
    cidfamilyname: Any = ...
    cidfontname: Any = ...
    cidfullname: Any = ...
    cidordering: Any = ...
    cidregistry: Any = ...
    cidsubfont: Any = ...
    cidsubfontcnt: Any = ...
    cidsubfontnames: Any = ...
    cidsupplement: Any = ...
    cidversion: Any = ...
    cidweight: Any = ...
    comment: Any = ...
    copyright: Any = ...
    creationtime: Any = ...
    cvt: Any = ...
    default_base_filename: Any = ...
    descent: Any = ...
    design_size: Any = ...
    em: Any = ...
    encoding: Any = ...
    familyname: Any = ...
    fondname: Any = ...
    fontlog: Any = ...
    fontname: Any = ...
    fullname: Any = ...
    gasp: Any = ...
    gasp_version: Any = ...
    gpos_lookups: Any = ...
    gsub_lookups: Any = ...
    guide: Any = ...
    hasvmetrics: Any = ...
    head_optimized_for_cleartype: Any = ...
    hhea_ascent: Any = ...
    hhea_ascent_add: Any = ...
    hhea_descent: Any = ...
    hhea_descent_add: Any = ...
    hhea_linegap: Any = ...
    horizontalBaseline: Any = ...
    is_cid: Any = ...
    is_quadratic: Any = ...
    iscid: Any = ...
    isnew: Any = ...
    italicangle: Any = ...
    layer_cnt: Any = ...
    layers: Any = ...
    loadState: Any = ...
    macstyle: Any = ...
    markClasses: Any = ...
    math: Any = ...
    maxp_FDEFs: Any = ...
    maxp_IDEFs: Any = ...
    maxp_maxStackDepth: Any = ...
    maxp_storageCnt: Any = ...
    maxp_twilightPtCnt: Any = ...
    maxp_zones: Any = ...
    multilayer: Any = ...
    onlybitmaps: Any = ...
    os2_capheight: Any = ...
    os2_codepages: Any = ...
    os2_family_class: Any = ...
    os2_fstype: Any = ...
    os2_panose: Any = ...
    os2_strikeypos: Any = ...
    os2_strikeysize: Any = ...
    os2_stylemap: Any = ...
    os2_subxoff: Any = ...
    os2_subxsize: Any = ...
    os2_subyoff: Any = ...
    os2_subysize: Any = ...
    os2_supxoff: Any = ...
    os2_supxsize: Any = ...
    os2_supyoff: Any = ...
    os2_supysize: Any = ...
    os2_typoascent: Any = ...
    os2_typoascent_add: Any = ...
    os2_typodescent: Any = ...
    os2_typodescent_add: Any = ...
    os2_typolinegap: Any = ...
    os2_unicoderanges: Any = ...
    os2_use_typo_metrics: Any = ...
    os2_vendor: Any = ...
    os2_version: Any = ...
    os2_weight: Any = ...
    os2_weight_width_slope_only: Any = ...
    os2_width: Any = ...
    os2_winascent: Any = ...
    os2_winascent_add: Any = ...
    os2_windescent: Any = ...
    os2_windescent_add: Any = ...
    os2_xheight: Any = ...
    path: Any = ...
    persistant: Any = ...
    persistent: Any = ...
    private: Any = ...
    privateState: Any = ...
    selection: Selection = ...
    sfd_path: Any = ...
    sfntRevision: Any = ...
    sfnt_names: Any = ...
    size_feature: Any = ...
    strokedfont: Any = ...
    strokewidth: Any = ...
    temporary: Any = ...
    texparameters: Any = ...
    uniqueid: Any = ...
    upos: Any = ...
    userdata: Any = ...
    uwidth: Any = ...
    version: Any = ...
    verticalBaseline: Any = ...
    vertical_origin: Any = ...
    vhea_linegap: Any = ...
    weight: Any = ...
    woffMajor: Any = ...
    woffMetadata: Any = ...
    woffMinor: Any = ...
    xHeight: Any = ...
    xuid: Any = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def addAnchorClass(self, *args, **kwargs) -> Any: ...
    def addContextualSubtable(self, *args, **kwargs) -> Any: ...
    def addExtrema(self, *args, **kwargs) -> Any: ...
    def addKerningClass(self, *args, **kwargs) -> Any: ...
    def addLookup(self, *args, **kwargs) -> Any: ...
    def addLookupSubtable(self, *args, **kwargs) -> Any: ...
    def addSmallCaps(self, *args, **kwargs) -> Any: ...
    def alterKerningClass(self, *args, **kwargs) -> Any: ...
    def appendSFNTName(self, *args, **kwargs) -> Any: ...
    def autoHint(self, *args, **kwargs) -> Any: ...
    def autoInstr(self, *args, **kwargs) -> Any: ...
    def autoKern(self, *args, **kwargs) -> Any: ...
    def autoTrace(self, *args, **kwargs) -> Any: ...
    def autoWidth(self, *args, **kwargs) -> Any: ...
    def build(self, *args, **kwargs) -> Any: ...
    def buildOrReplaceAALTFeatures(self, *args, **kwargs) -> Any: ...
    def canonicalContours(self, *args, **kwargs) -> Any: ...
    def canonicalStart(self, *args, **kwargs) -> Any: ...
    def changeWeight(self, *args, **kwargs) -> Any: ...
    def cidConvertByCmap(self, *args, **kwargs) -> Any: ...
    def cidConvertTo(self, *args, **kwargs) -> Any: ...
    def cidFlatten(self, *args, **kwargs) -> Any: ...
    def cidFlattenByCMap(self, *args, **kwargs) -> Any: ...
    def cidInsertBlankSubFont(self, *args, **kwargs) -> Any: ...
    def cidRemoveSubFont(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def clearSpecialData(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    def cluster(self, *args, **kwargs) -> Any: ...
    def compareFonts(self, *args, **kwargs) -> Any: ...
    def condenseExtend(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def copyReference(self, *args, **kwargs) -> Any: ...
    def correctDirection(self, *args, **kwargs) -> Any: ...
    def correctReferences(self, *args, **kwargs) -> Any: ...
    def createChar(self, *args, **kwargs) -> Any: ...
    def createInterpolatedGlyph(self, *args, **kwargs) -> Any: ...
    def createMappedChar(self, *args, **kwargs) -> Any: ...
    def cut(self, *args, **kwargs) -> Any: ...
    def find(self, *args, **kwargs) -> Any: ...
    def findEncodingSlot(self, *args, **kwargs) -> Any: ...
    def generate(self, *args, **kwargs) -> Any: ...
    def generateFeatureFile(self, *args, **kwargs) -> Any: ...
    def generateTtc(self, *args, **kwargs) -> Any: ...
    def genericGlyphChange(self, *args, **kwargs) -> Any: ...
    def getKerningClass(self, *args, **kwargs) -> Any: ...
    def getLookupInfo(self, *args, **kwargs) -> Any: ...
    def getLookupOfSubtable(self, *args, **kwargs) -> Any: ...
    def getLookupSubtableAnchorClasses(self, *args, **kwargs) -> Any: ...
    def getLookupSubtables(self, *args, **kwargs) -> Any: ...
    def getSubtableOfAnchor(self, *args, **kwargs) -> Any: ...
    def getTableData(self, *args, **kwargs) -> Any: ...
    def glyphs(self, *args, **kwargs) -> Any: ...
    def importBitmaps(self, *args, **kwargs) -> Any: ...
    def importLookups(self, *args, **kwargs) -> Any: ...
    def interpolateFonts(self, *args, **kwargs) -> Any: ...
    def intersect(self, *args, **kwargs) -> Any: ...
    def isKerningClass(self, *args, **kwargs) -> Any: ...
    def isVerticalKerning(self, *args, **kwargs) -> Any: ...
    def italicize(self, *args, **kwargs) -> Any: ...
    def lookupSetFeatureList(self, *args, **kwargs) -> Any: ...
    def lookupSetFlags(self, *args, **kwargs) -> Any: ...
    def lookupSetStoreLigatureInAfm(self, *args, **kwargs) -> Any: ...
    def mergeFeature(self, *args, **kwargs) -> Any: ...
    def mergeFonts(self, *args, **kwargs) -> Any: ...
    def mergeKern(self, *args, **kwargs) -> Any: ...
    def mergeLookupSubtables(self, *args, **kwargs) -> Any: ...
    def mergeLookups(self, *args, **kwargs) -> Any: ...
    def nltransform(self, *args, **kwargs) -> Any: ...
    def paste(self, *args, **kwargs) -> Any: ...
    def pasteInto(self, *args, **kwargs) -> Any: ...
    def printSample(self, *args, **kwargs) -> Any: ...
    def randomText(self, *args, **kwargs) -> Any: ...
    def reencode(self, *args, **kwargs) -> Any: ...
    def regenBitmaps(self, *args, **kwargs) -> Any: ...
    def removeAnchorClass(self, *args, **kwargs) -> Any: ...
    def removeGlyph(self, *args, **kwargs) -> Any: ...
    def removeLookup(self, *args, **kwargs) -> Any: ...
    def removeLookupSubtable(self, *args, **kwargs) -> Any: ...
    def removeOverlap(self, *args, **kwargs) -> Any: ...
    def replaceAll(self, *args, **kwargs) -> Any: ...
    def replaceWithReference(self, *args, **kwargs) -> Any: ...
    def revert(self, *args, **kwargs) -> Any: ...
    def revertFromBackup(self, *args, **kwargs) -> Any: ...
    def round(self, *args, **kwargs) -> Any: ...
    def save(self, *args, **kwargs) -> Any: ...
    def saveNamelist(self, *args, **kwargs) -> Any: ...
    def setTableData(self, *args, **kwargs) -> Any: ...
    def simplify(self, *args, **kwargs) -> Any: ...
    def stroke(self, *args, **kwargs) -> Any: ...
    def transform(self, *args, **kwargs) -> Any: ...
    def unlinkReferences(self, *args, **kwargs) -> Any: ...
    def validate(self, *args, **kwargs) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...


class glyph:
    activeLayer: Any = ...
    altuni: Any = ...
    anchorPoints: Any = ...
    anchorPointsWithSel: Any = ...
    background: Any = ...
    changed: Any = ...
    codepoint: Any = ...
    color: Any = ...
    comment: Any = ...
    dhints: Any = ...
    encoding: Any = ...
    font: Font = ...
    foreground: Any = ...
    glyphclass: Any = ...
    glyphname: Any = ...
    hhints: Any = ...
    horizontalComponentItalicCorrection: Any = ...
    horizontalComponents: Any = ...
    horizontalVariants: Any = ...
    isExtendedShape: Any = ...
    italicCorrection: Any = ...
    layer_cnt: Any = ...
    layerrefs: Any = ...
    layers: Any = ...
    lcarets: Any = ...
    left_side_bearing: Any = ...
    manualHints: Any = ...
    mathKern: Any = ...
    originalgid: Any = ...
    persistant: Any = ...
    persistent: Any = ...
    references: Any = ...
    right_side_bearing: Any = ...
    script: Any = ...
    temporary: Any = ...
    texdepth: Any = ...
    texheight: Any = ...
    topaccent: Any = ...
    ttinstrs: Any = ...
    unicode: Any = ...
    unlinkRmOvrlpSave: Any = ...
    user_decomp: Any = ...
    userdata: Any = ...
    validation_state: Any = ...
    verticalComponentItalicCorrection: Any = ...
    verticalComponents: Any = ...
    verticalVariants: Any = ...
    vhints: Any = ...
    vwidth: Any = ...
    width: Any = ...
    __hash__: Any = ...
    def addAnchorPoint(self, *args, **kwargs) -> Any: ...
    def addExtrema(self, *args, **kwargs) -> Any: ...
    def addHint(self, *args, **kwargs) -> Any: ...
    def addPosSub(self, *args, **kwargs) -> Any: ...
    def addReference(self, *args, **kwargs) -> Any: ...
    def appendAccent(self, *args, **kwargs) -> Any: ...
    def autoHint(self, *args, **kwargs) -> Any: ...
    def autoInstr(self, *args, **kwargs) -> Any: ...
    def autoTrace(self, *args, **kwargs) -> Any: ...
    def boundingBox(self, *args, **kwargs) -> Any: ...
    def build(self, *args, **kwargs) -> Any: ...
    def canonicalContours(self, *args, **kwargs) -> Any: ...
    def canonicalStart(self, *args, **kwargs) -> Any: ...
    def changeWeight(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def cluster(self, *args, **kwargs) -> Any: ...
    def condenseExtend(self, *args, **kwargs) -> Any: ...
    def correctDirection(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def exclude(self, *args, **kwargs) -> Any: ...
    def export(self, *args, **kwargs) -> Any: ...
    def getPosSub(self, *args, **kwargs) -> Any: ...
    def glyphPen(self, *args, **kwargs) -> Any: ...
    def importOutlines(self, *args, **kwargs) -> Any: ...
    def intersect(self, *args, **kwargs) -> Any: ...
    def isWorthOutputting(self, *args, **kwargs) -> Any: ...
    def nltransform(self, *args, **kwargs) -> Any: ...
    def preserveLayerAsUndo(self, *args, **kwargs) -> Any: ...
    def removeOverlap(self, *args, **kwargs) -> Any: ...
    def removePosSub(self, *args, **kwargs) -> Any: ...
    def round(self, *args, **kwargs) -> Any: ...
    def selfIntersects(self, *args, **kwargs) -> Any: ...
    def setLayer(self, *args, **kwargs) -> Any: ...
    def simplify(self, *args, **kwargs) -> Any: ...
    def stroke(self, *args, **kwargs) -> Any: ...
    def transform(self, *args, **kwargs) -> Any: ...
    def unlinkRef(self, *args, **kwargs) -> Any: ...
    def unlinkThisGlyph(self, *args, **kwargs) -> Any: ...
    def useRefsMetrics(self, *args, **kwargs) -> Any: ...
    def validate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...


class glyphPen:
    def addComponent(self, *args, **kwargs) -> Any: ...
    def closePath(self, *args, **kwargs) -> Any: ...
    def curveTo(self, *args, **kwargs) -> Any: ...
    def endPath(self, *args, **kwargs) -> Any: ...
    def lineTo(self, *args, **kwargs) -> Any: ...
    def moveTo(self, *args, **kwargs) -> Any: ...
    def qCurveTo(self, *args, **kwargs) -> Any: ...


class layer:
    is_quadratic: Any = ...
    __hash__: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addExtrema(self, *args, **kwargs) -> Any: ...
    def boundingBox(self, *args, **kwargs) -> Any: ...
    def cluster(self, *args, **kwargs) -> Any: ...
    def correctDirection(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def dup(self, *args, **kwargs) -> Any: ...
    def exclude(self, *args, **kwargs) -> Any: ...
    def export(self, *args, **kwargs) -> Any: ...
    def interpolateNewLayer(self, *args, **kwargs) -> Any: ...
    def intersect(self, *args, **kwargs) -> Any: ...
    def isEmpty(self, *args, **kwargs) -> Any: ...
    def nltransform(self, *args, **kwargs) -> Any: ...
    def removeOverlap(self, *args, **kwargs) -> Any: ...
    def reverseDirection(self, *args, **kwargs) -> Any: ...
    def round(self, *args, **kwargs) -> Any: ...
    def selfIntersects(self, *args, **kwargs) -> Any: ...
    def similar(self, *args, **kwargs) -> Any: ...
    def simplify(self, *args, **kwargs) -> Any: ...
    def stemControl(self, *args, **kwargs) -> Any: ...
    def stroke(self, *args, **kwargs) -> Any: ...
    def transform(self, *args, **kwargs) -> Any: ...
    def xBoundsAtY(self, *args, **kwargs) -> Any: ...
    def yBoundsAtX(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __iadd__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class layer_array:
    font: Any = ...
    glyph: Any = ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class layerinfo:
    font: Any = ...
    is_background: Any = ...
    is_quadratic: Any = ...
    name: Any = ...


class layerinfo_array:
    font: Any = ...
    def add(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class math:
    AccentBaseHeight: Any = ...
    AxisHeight: Any = ...
    DelimitedSubFormulaMinHeight: Any = ...
    DisplayOperatorMinHeight: Any = ...
    FlattenedAccentBaseHeight: Any = ...
    FractionDenominatorDisplayStyleGapMin: Any = ...
    FractionDenominatorDisplayStyleShiftDown: Any = ...
    FractionDenominatorGapMin: Any = ...
    FractionDenominatorShiftDown: Any = ...
    FractionNumeratorDisplayStyleGapMin: Any = ...
    FractionNumeratorDisplayStyleShiftUp: Any = ...
    FractionNumeratorGapMin: Any = ...
    FractionNumeratorShiftUp: Any = ...
    FractionRuleThickness: Any = ...
    LowerLimitBaselineDropMin: Any = ...
    LowerLimitGapMin: Any = ...
    MathLeading: Any = ...
    MinConnectorOverlap: Any = ...
    OverbarExtraAscender: Any = ...
    OverbarRuleThickness: Any = ...
    OverbarVerticalGap: Any = ...
    RadicalDegreeBottomRaisePercent: Any = ...
    RadicalDisplayStyleVerticalGap: Any = ...
    RadicalExtraAscender: Any = ...
    RadicalKernAfterDegree: Any = ...
    RadicalKernBeforeDegree: Any = ...
    RadicalRuleThickness: Any = ...
    RadicalVerticalGap: Any = ...
    ScriptPercentScaleDown: Any = ...
    ScriptScriptPercentScaleDown: Any = ...
    SkewedFractionHorizontalGap: Any = ...
    SkewedFractionVerticalGap: Any = ...
    SpaceAfterScript: Any = ...
    StackBottomDisplayStyleShiftDown: Any = ...
    StackBottomShiftDown: Any = ...
    StackDisplayStyleGapMin: Any = ...
    StackGapMin: Any = ...
    StackTopDisplayStyleShiftUp: Any = ...
    StackTopShiftUp: Any = ...
    StretchStackBottomShiftDown: Any = ...
    StretchStackGapAboveMin: Any = ...
    StretchStackGapBelowMin: Any = ...
    StretchStackTopShiftUp: Any = ...
    SubSuperscriptGapMin: Any = ...
    SubscriptBaselineDropMin: Any = ...
    SubscriptShiftDown: Any = ...
    SubscriptTopMax: Any = ...
    SuperscriptBaselineDropMax: Any = ...
    SuperscriptBottomMaxWithSubscript: Any = ...
    SuperscriptBottomMin: Any = ...
    SuperscriptShiftUp: Any = ...
    SuperscriptShiftUpCramped: Any = ...
    UnderbarExtraDescender: Any = ...
    UnderbarRuleThickness: Any = ...
    UnderbarVerticalGap: Any = ...
    UpperLimitBaselineRiseMin: Any = ...
    UpperLimitGapMin: Any = ...
    def clear(self, *args, **kwargs) -> Any: ...
    def exists(self, *args, **kwargs) -> Any: ...


class mathKern:
    bottomLeft: Any = ...
    bottomRight: Any = ...
    topLeft: Any = ...
    topRight: Any = ...


class point:
    interpolated: Any = ...
    name: Any = ...
    on_curve: Any = ...
    selected: Any = ...
    type: Any = ...
    x: Any = ...
    y: Any = ...
    __hash__: Any = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def dup(self, *args, **kwargs) -> Any: ...
    def transform(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...


class private:
    def guess(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class references:
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class selection:
    byGlyphs: Iterator[Glyph] = ...
    font: Font = ...
    def all(self, *args, **kwargs) -> Any: ...
    def changed(self, *args, **kwargs) -> Any: ...
    def invert(self, *args, **kwargs) -> Any: ...
    def none(self, *args, **kwargs) -> Any: ...
    def select(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


Font = font
Selection = selection
Glyph = glyph