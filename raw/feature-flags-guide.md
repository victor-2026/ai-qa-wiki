**Source:** [Qase Blog](https://qase.io/blog/feature-flags/)
**Date:** 2024-10-10
**Author:** Vitaly Sharovatov

---

# Feature Flags: When and How to Use

## What Are Feature Flags

Technique enabling/disabling features **without deploying new code**. Also called: feature toggles, flippers, release toggles.

Separates **deployment** from **release**.

## Use Cases

### 1. Canary Releases
Roll out to small subset → identify issues early → reduce impact

### 2. Testing in Production / Dogfooding
Test directly in production environment → find issues staging misses

### 3. Rollbacks / Killswitches
Instant disable without hotfix → toggle off if problems arise

### 4. A/B Testing
Different variations for different segments → compare performance

### 5. Incremental Rollouts
Gradually increase user access → monitor before full release

## Benefits

| Benefit | Description |
|---------|-------------|
| **Risk reduction** | Separate deployment from release |
| **Faster feedback** | Real user feedback via canary/A/B testing |
| **No rushed hotfixes** | Toggle off vs deploy changes |

## Implementation Approaches

### Simple (Occasional Use)
```python
if feature_config.get('new_feature'):
    # new feature code
```
- Limited: no monitoring, no gradual rollout
- Good for: rare feature flags

### Full System (Continuous Use)
- Centralized system for all flags
- Fast, reliable (Redis in-memory)
- Support gradual rollout, user segmentation
- Tools: Unleash, FeatureHub

## Best Practices

1. **Define scope** — global, per-user, per-group
2. **Default: "off"** — deploy first, enable later
3. **Test both states** — enabled AND disabled
4. **Set expiry criteria** — when to make permanent
5. **Clean up** — remove flag after feature is stable

## Qase Example

- Flags stored in Redis (fast, in-memory)
- Hierarchical: workspace > user
- Frontend checks flag → renders appropriate component
- Remove flag when feature is permanent

## Key Takeaway

> "Feature flags separate deployment from release, minimizing risks involved in deploying new features."

## Related

- Canary Testing
- A/B Testing
- Dogfooding
- Continuous Deployment
