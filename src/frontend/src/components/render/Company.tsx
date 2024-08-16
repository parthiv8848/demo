import { ReactNode } from 'react';

import { InstanceRenderInterface, RenderInlineModel } from './Instance';

/**
 * Inline rendering of a single Address instance
 */
export function RenderAddress({
  instance
}: Readonly<InstanceRenderInterface>): ReactNode {
  let text = [
    instance.country,
    instance.postal_code,
    instance.postal_city,
    instance.province,
    instance.line1,
    instance.line2
  ]
    .filter(Boolean)
    .join(', ');

  return <RenderInlineModel primary={instance.title} secondary={text} />;
}

/**
 * Inline rendering of a single Company instance
 */
export function RenderCompany({
  instance
}: Readonly<InstanceRenderInterface>): ReactNode {
  // TODO: Handle URL

  return (
    <RenderInlineModel
      image={instance.thumnbnail || instance.image}
      primary={instance.name}
      secondary={instance.description}
    />
  );
}

/**
 * Inline rendering of a single Contact instance
 */
export function RenderContact({
  instance
}: Readonly<InstanceRenderInterface>): ReactNode {
  return <RenderInlineModel primary={instance.name} />;
}

/**
 * Inline rendering of a single SupplierPart instance
 */
export function RenderSupplierPart({
  instance
}: Readonly<InstanceRenderInterface>): ReactNode {
  // TODO: handle URL

  let supplier = instance.supplier_detail ?? {};
  let part = instance.part_detail ?? {};

  return (
    <RenderInlineModel
      primary={supplier?.name}
      secondary={instance.SKU}
      image={part?.thumbnail ?? part?.image}
      suffix={part.full_name}
    />
  );
}

/**
 * Inline rendering of a single ManufacturerPart instance
 */
export function RenderManufacturerPart({
  instance
}: Readonly<InstanceRenderInterface>): ReactNode {
  let part = instance.part_detail ?? {};
  let manufacturer = instance.manufacturer_detail ?? {};

  return (
    <RenderInlineModel
      primary={manufacturer.name}
      secondary={instance.MPN}
      suffix={part.full_name}
      image={manufacturer?.thumnbnail ?? manufacturer.image}
    />
  );
}
