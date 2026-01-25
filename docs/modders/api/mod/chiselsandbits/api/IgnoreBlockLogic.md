--- 
title: IgnoreBlockLogic
aside: false 
---
_Package:_ [mod.chiselsandbits.api](index.md)  
# Annotation_type IgnoreBlockLogic  
**All Extended Interfaces:**  
Annotation  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/annotation/Retention.html" title="class or interface in java.lang.annotation" class="external-link">@Retention</a>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/annotation/RetentionPolicy.html#RUNTIME" title="class or interface in java.lang.annotation" class="external-link">RUNTIME</a>)<br/>  
</span><span class="modifiers">public @interface </span><span class="element-name type-name-label">IgnoreBlockLogic</span></div>  

  

<div class="block">When checking for blocks to allow for chiseling Chisels and Bits checks various methods...

 hasTileEntity, getTickRandomly, quantityDropped, quantityDroppedWithBonus,
 onEntityCollidedWithBlock, and isFullBlock

 If you include this annotation or use the tag, you can force Chisels and Bits to
 overlook these custom implementations, please use with care and test before
 releasing usage.</div>
  

<dl class="notes"></dl>  

  

  

  

  

  

  

  

